import pandas as pd

# Titanic ma'lumotlarini yuklash
titanic_df = pd.read_excel("titanic.xlsx")

# 1. Tirik qolganlarni filtrlash
def filter_survivors(df):
    return df[df["Survived"] == 1]

# 2. Age ustunidagi bo‘sh joylarni o‘rtacha qiymat bilan to‘ldirish
def fill_missing_age(df):
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df

# 3. Fare ni Age ga bo‘lish orqali yangi ustun qo‘shish
def add_fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

# Pipeline qo‘llash
titanic_processed = (titanic_df
                     .pipe(filter_survivors)
                     .pipe(fill_missing_age)
                     .pipe(add_fare_per_age))

# Natijani chiqarish
print("\n--- TITANIC PIPELINE: Yangi ma'lumotlar ---")
print(titanic_processed[["Survived", "Age", "Fare", "Fare_Per_Age"]].head())