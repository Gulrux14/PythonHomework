import pandas as pd

# 1. iris.json DataFrame
iris_df = pd.read_json("iris.json")

# Column names to lowercase
iris_df.columns = iris_df.columns.str.lower()
print("Columns renamed to lowercase:", iris_df.columns.tolist())

# Selecting only sepal_length and sepal_width
iris_selected = iris_df[["sepal_length", "sepal_width"]]
print(iris_selected.head())

# 2. titanic.xlsx DataFrame
titanic_df = pd.read_excel("titanic.xlsx")

# Filter passengers older than 30
titanic_filtered = titanic_df[titanic_df["Age"] > 30]
print("Passengers older than 30:", titanic_filtered.shape[0])

# Count male and female passengers
gender_counts = titanic_df["Sex"].value_counts()
print("Number of male and female passengers:")
print(gender_counts)

# 3. Flights parquet file
flights_df = pd.read_parquet("flights.parquet")

# Extracting origin, dest, and carrier columns
flights_selected = flights_df[["origin", "dest", "carrier"]]
print(flights_selected.head())

# Finding the number of unique destinations
unique_destinations = flights_df["dest"].nunique()
print("Number of unique destinations:", unique_destinations)

# 4. movie.csv DataFrame
movie_df = pd.read_csv("movie.csv")

# Filter movies longer than 120 minutes
long_movies = movie_df[movie_df["duration"] > 120]

# Sort by director_facebook_likes in descending order
sorted_movies = long_movies.sort_values(by="director_facebook_likes", ascending=False)
print(sorted_movies.head())