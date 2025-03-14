import numpy as np

# Fahrenheitdan Celsiusga o‘tkazish funksiyasi
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9  # 5/9 hisob-kitobi to‘g‘ri

# Funksiyani vektorizatsiya qilish
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

# Fahrenheit haroratlari ro‘yxati
fahrenheit_temps = np.array([32, 68, 100, 212, 77])

# Celsiusga aylantirish
celsius_temps = vectorized_conversion(fahrenheit_temps)

# Natijani chiqarish
print(list(celsius_temps))