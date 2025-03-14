import numpy as np
import matplotlib.pyplot as plt

# X qiymatlarini yaratish
x = np.linspace(-10, 10, 100)

# Funksiya qiymatlari
y = x**2 - 4*x + 4

# Grafikni chizish
plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 4$", color="blue")

# O‘qlarni belgilash
plt.xlabel("x qiymatlari")
plt.ylabel("f(x) qiymatlari")
plt.title("Kvadratik funksiya grafigi")

# Grid va legenda qo‘shish
plt.grid(True)
plt.legend()

# Grafikni ko‘rsatish
plt.show()