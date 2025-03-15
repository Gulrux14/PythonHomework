import pandas as pd

# 1. iris.json DataFrame
iris_df = pd.read_json("iris.json")

# Calculate mean, median, and standard deviation for numerical columns
iris_stats = iris_df.describe().T
iris_stats["median"] = iris_df.median()
print("Iris dataset statistics:\n", iris_stats)

# 2. titanic.xlsx DataFrame
titanic_df = pd.read_excel("titanic.xlsx")

# Find min, max, and sum of passenger ages
age_min = titanic_df["Age"].min()
age_max = titanic_df["Age"].max()
age_sum = titanic_df["Age"].sum()
print(f"Titanic passengers' age - Min: {age_min}, Max: {age_max}, Sum: {age_sum}")

# 3. movie.csv DataFrame
movie_df = pd.read_csv("movie.csv")

# Identify the director with the highest total director_facebook_likes
top_director = movie_df.groupby("director_name")["director_facebook_likes"].sum().idxmax()
print("Director with highest total Facebook likes:", top_director)

# Find the 5 longest movies and their directors
longest_movies = movie_df.nlargest(5, "duration")[["title", "duration", "director_name"]]
print("Top 5 longest movies:\n", longest_movies)

# 4. Flights parquet file
flights_df = pd.read_parquet("flights.parquet")

# Check for missing values
missing_values = flights_df.isnull().sum()
print("Missing values in Flights dataset:\n", missing_values)

# Fill missing values in a numerical column (e.g., "air_time") with its mean
if "air_time" in flights_df.columns:
    flights_df["air_time"].fillna(flights_df["air_time"].mean(), inplace=True)
    print("Missing values in 'air_time' column filled with mean.")