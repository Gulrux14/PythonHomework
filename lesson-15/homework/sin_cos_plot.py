import numpy as np
import matplotlib.pyplot as plt

# X qiymatlarini yaratish (0 dan 2π gacha)
x = np.linspace(0, 2 * np.pi, 100)

# Funksiya qiymatlari
y_sin = np.sin(x)
y_cos = np.cos(x)

# Grafikni chizish
plt.plot(x, y_sin, linestyle='-', marker='o', color='b', label=r"$\sin(x)$")
plt.plot(x, y_cos, linestyle='--', marker='s', color='r', label=r"$\cos(x)$")

# O‘qlarni belgilash
plt.xlabel("x qiymatlari")
plt.ylabel("y qiymatlari")
plt.title("Sinus va Kosinus grafigi")

# Grid va legenda qo‘shish
plt.grid(True)
plt.legend()

# Grafikni ko‘rsatish
plt.show()