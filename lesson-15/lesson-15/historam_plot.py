import numpy as np
import matplotlib.pyplot as plt

# 1000 ta normal taqsimotga ega tasodifiy sonlar (mean=0, std=1)
data = np.random.normal(loc=0, scale=1, size=1000)

# Histogram chizish
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)

# Sarlavha va o‘qlarni belgilash
plt.title("Normal Taqsimot Histogrami")
plt.xlabel("Qiymatlar")
plt.ylabel("Frekvensiya")

# Grid qo‘shish
plt.grid(True, linestyle='--', alpha=0.6)

# Grafikni ko‘rsatish
plt.show()