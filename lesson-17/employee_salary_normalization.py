import pandas as pd

# Employee ma'lumotlarini yuklash
employee_df = pd.read_csv("employee.csv")

# Normallashtirish funktsiyasi
def normalize_salary(group):
    return (group - group.min()) / (group.max() - group.min())

# Bo‘lim bo‘yicha maoshlarni normallashtirish
employee_df["Normalized_Salary"] = employee_df.groupby("Department")["Salary"].transform(normalize_salary)

# Natijani chiqarish
print("\n--- EMPLOYEE: Normallashtirilgan maoshlar ---")
print(employee_df[["Department", "Salary", "Normalized_Salary"]].head())