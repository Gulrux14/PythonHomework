import sqlite3

# Step 1: Create Database and Table
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")

# Step 2: Insert Data
cursor.executemany("""
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Step 3: Update Data
cursor.execute("""
    UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'
""")

# Step 4: Query Data
cursor.execute("""
    SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
bajoran_characters = cursor.fetchall()
print("Bajoran Characters:", bajoran_characters)

# Step 5: Delete Data
cursor.execute("""
    DELETE FROM Roster WHERE Age > 100
""")

# Bonus Task: Add a New Column and Update Data
cursor.execute("""
    ALTER TABLE Roster ADD COLUMN Rank TEXT
""")

cursor.executemany("""
    UPDATE Roster SET Rank = ? WHERE Name = ?
""", [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])

# Advanced Query: Retrieve Sorted Data
cursor.execute("""
    SELECT * FROM Roster ORDER BY Age DESC
""")
sorted_characters = cursor.fetchall()
print("Sorted Characters:", sorted_characters)

# Commit and close the connection
conn.commit()
conn.close()