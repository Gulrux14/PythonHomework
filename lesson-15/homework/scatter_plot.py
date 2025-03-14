import numpy as np
import matplotlib.pyplot as plt

# 100 ta tasodifiy (x, y) koordinatalarni yaratish
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

# Scatter plot chizish
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=np.random.rand(100), marker='o', edgecolors='black', alpha=0.7)

# Sarlavha va o‘qlarni belgilash
plt.title("Tasodifiy 2D Scatter Plot")
plt.xlabel("X koordinata")
plt.ylabel("Y koordinata")

# Grid qo‘shish
plt.grid(True, linestyle='--', alpha=0.6)

# Grafikni ko‘rsatish
plt.show()