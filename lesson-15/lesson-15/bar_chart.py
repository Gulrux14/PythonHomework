import numpy as np
import matplotlib.pyplot as plt

# Mahsulot nomlari va sotuv qiymatlari
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

# Ranglar ro‘yxati
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Bar chart yaratish
plt.figure(figsize=(8, 6))
plt.bar(products, sales, color=colors, edgecolor='black')

# Sarlavha va o‘qlarni belgilash
plt.title("Mahsulot Sotuvlari")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotuv miqdori")

# Grid qo‘shish
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Grafikni ko‘rsatish
plt.show()