import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# X va Y uchun massivlarni yaratish
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Funksiyani hisoblash
Z = np.cos(X**2 + Y**2)

# 3D rasm yaratish
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Sirtni chizish
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Rangsiz o‘qlarga sarlavha qo‘shish
ax.set_title("3D Surface Plot of $f(x, y) = \cos(x^2 + y^2)$")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(X, Y)")

# Rang shkalasi qo‘shish
fig.colorbar(surf, ax=ax, shrink=0.6, aspect=10)

# Grafikni ko‘rsatish
plt.show()