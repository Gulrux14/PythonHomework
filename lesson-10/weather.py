import requests

# OpenWeatherMap API kalitingizni shu yerga joylang
API_KEY = "6cdf217ba42e0e1e19132f660e101ba7"

# Shahar nomini kiriting
city = "Tashkent"

# API so‘rovi uchun URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# API ga so‘rov yuborish
response = requests.get(url)
data = response.json()

# Ma'lumotlarni chiqarish
if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    
    print(f"Shahar: {city}")
    print(f"Harorat: {temperature}°C")
    print(f"Namlik: {humidity}%")
    print(f"Ob-havo tavsifi: {weather_desc}")
else:
    print("Ob-havo ma'lumotlarini olishda xatolik yuz berdi.")