import sqlite3
import pandas as pd

# 1. SQLite database (chinook.db)
conn = sqlite3.connect("chinook.db")  # Fayl mavjud bo‘lishi kerak
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print(customers_df.head(10))  # Dastlabki 10 qatorni chiqarish
conn.close()

# 2. JSON file (iris.json)
iris_df = pd.read_json("iris.json")  # JSON fayl mavjud bo‘lishi kerak
print("Iris dataset shape:", iris_df.shape)
print("Column names:", iris_df.columns.tolist())

# 3. Excel file (titanic.xlsx)
titanic_df = pd.read_excel("titanic.xlsx")  # Excel fayl mavjud bo‘lishi kerak
print(titanic_df.head())  # Dastlabki 5 qatorni chiqarish

# 4. Parquet file (flights.parquet)
flights_df = pd.read_parquet("flights.parquet")  # Parquet fayl mavjud bo‘lishi kerak
print(flights_df.info())  # Malumotlar haqida umumiy ma’lumot

# 5. CSV file (movie.csv)
movie_df = pd.read_csv("movie.csv")  # CSV fayl mavjud bo‘lishi kerak
print(movie_df.sample(10))  # Tasodifiy 10 qatorni chiqarish