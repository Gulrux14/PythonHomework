import sqlite3
import pandas as pd

### 1️⃣ CHINOOK DATABASE: INNER JOIN ###

# Chinook bazasiga ulanish
conn = sqlite3.connect("chinook.db")

# Jadvallarni yuklash
customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)

# INNER JOIN: mijozlar va ularning fakturalari
merged_df = pd.merge(customers, invoices, on="CustomerId", how="inner")

# Har bir mijoz uchun faktura sonini hisoblash
invoice_counts = merged_df.groupby(["CustomerId", "FirstName", "LastName"]).size().reset_index(name="TotalInvoices")

# Natijani chiqarish
print("\n--- CHINOOK: Har bir mijoz uchun faktura soni ---")
print(invoice_counts.head())

# Bazani yopish
conn.close()


### 2️⃣ MOVIE DATA: LEFT JOIN VA FULL OUTER JOIN ###

# CSV faylni yuklash
movies = pd.read_csv("movie.csv")

# 1-qism: Faqat "director_name" va "color"
df1 = movies[["director_name", "color"]].dropna()

# 2-qism: Faqat "director_name" va "num_critic_for_reviews"
df2 = movies[["director_name", "num_critic_for_reviews"]].dropna()

# LEFT JOIN
left_join = pd.merge(df1, df2, on="director_name", how="left")

# FULL OUTER JOIN
full_outer_join = pd.merge(df1, df2, on="director_name", how="outer")

# Natijalar sonini chiqarish