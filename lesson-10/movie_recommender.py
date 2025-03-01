import requests
import random

# TMDb API kalitini shu joyga kiriting
API_KEY = "6743b5fab8375a1df376fe0b8ab8c2fc"

# Foydalanuvchidan janr so‘rash
genre_name = input("Qaysi janrdagi filmni xohlaysiz? (masalan: Action, Comedy, Horror): ")

# Janr ID larini olish
genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
genre_response = requests.get(genre_url).json()

# Janr nomini ID ga aylantirish
genre_id = None
for genre in genre_response["genres"]:
    if genre["name"].lower() == genre_name.lower():
        genre_id = genre["id"]
        break

if genre_id:
    # Ushbu janrdagi filmlarni olish
    movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    movies_response = requests.get(movies_url).json()

    # Filmlar ro‘yxatidan tasodifiy bittasini tanlash
    if movies_response["results"]:
        random_movie = random.choice(movies_response["results"])
        print(f"\nSizga tavsiya qilinadigan film: {random_movie['title']}")
        print(f"Tarixi: {random_movie['overview']}")
    else:
        print("Ushbu janr bo‘yicha film topilmadi.")
else:
    print("Noto‘g‘ri janr kiritildi yoki janr mavjud emas.")