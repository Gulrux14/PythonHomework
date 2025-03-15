import pandas as pd

# Movie ma'lumotlarini yuklash
movies_df = pd.read_csv("movie.csv")

# Davomiylikni tasniflovchi funktsiya
def classify_duration(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"

# Apply orqali yangi ustun qo‘shamiz
movies_df["Duration_Category"] = movies_df["duration"].apply(classify_duration)

# Natijani chiqarish
print("\n--- MOVIE: Duration_Category ustuni bilan yangilangan jadval ---")
print(movies_df[["duration", "Duration_Category"]].head())