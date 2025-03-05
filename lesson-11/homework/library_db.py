import sqlite3

# Step 1: Create Database and Table
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
""")

# Step 2: Insert Data
cursor.executemany("""
    INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

# Step 3: Update Data
cursor.execute("""
    UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'
""")

# Step 4: Query Data
cursor.execute("""
    SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
""")
dystopian_books = cursor.fetchall()
print("Dystopian Books:", dystopian_books)

# Step 5: Delete Data
cursor.execute("""
    DELETE FROM Books WHERE Year_Published < 1950
""")

# Bonus Task: Add a New Column and Update Data
cursor.execute("""
    ALTER TABLE Books ADD COLUMN Rating REAL
""")

cursor.executemany("""
    UPDATE Books SET Rating = ? WHERE Title = ?
""", [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
])

# Advanced Query: Retrieve Sorted Data
cursor.execute("""
    SELECT * FROM Books ORDER BY Year_Published ASC
""")
sorted_books = cursor.fetchall()
print("Sorted Books:", sorted_books)

# Commit and close the connection
conn.commit()
conn.close()