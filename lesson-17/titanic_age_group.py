import pandas as pd

# Titanic ma'lumotlarini yuklash
titanic_df = pd.read_excel("titanic.xlsx")

# Yangi funktsiya yaratamiz
def classify_age(age):
    return "Child" if age < 18 else "Adult"

# Apply orqali yangi ustun qo‘shamiz
titanic_df["Age_Group"] = titanic_df["Age"].apply(classify_age)

# Natijani chiqarish
print("\n--- TITANIC: Age_Group ustuni bilan yangilangan jadval ---")
print(titanic_df[["Age", "Age_Group"]].head())