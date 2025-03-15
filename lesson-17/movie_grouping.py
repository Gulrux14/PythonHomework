import pandas as pd

# Movie ma'lumotlarini yuklash
movies_df = pd.read_csv("movie.csv")

# color va director_name bo‘yicha guruhlash
grouped_movies = movies_df.groupby(["color", "director_name"]).agg(
    Total_Critic_Reviews=("num_critic_for_reviews", "sum"),
    Average_Duration=("duration", "mean")
).reset_index()

# Natijani chiqarish
print("\n--- MOVIE: Rang va rejissyor bo‘yicha guruhlangan statistikalar ---")
print(grouped_movies.head())