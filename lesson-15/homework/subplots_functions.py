import numpy as np
import matplotlib.pyplot as plt

# X qiymatlari
x = np.linspace(-2, 2, 100)  # f(x) = x^3 va f(x) = sin(x) uchun
x_positive = np.linspace(0, 2, 100)  # f(x) = e^x va f(x) = log(x+1) uchun

# Funksiya qiymatlari
y_cube = x**3
y_sin = np.sin(x)
y_exp = np.exp(x_positive)
y_log = np.log(x_positive + 1)

# Subplotlarni yaratish
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 1 - f(x) = x^3
axs[0, 0].plot(x, y_cube, color='b')
axs[0, 0].set_title(r"$f(x) = x^3$")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("y")
axs[0, 0].grid(True)

# 2 - f(x) = sin(x)
axs[0, 1].plot(x, y_sin, color='r')
axs[0, 1].set_title(r"$f(x) = \sin(x)$")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("y")
axs[0, 1].grid(True)

# 3 - f(x) = e^x
axs[1, 0].plot(x_positive, y_exp, color='g')
axs[1, 0].set_title(r"$f(x) = e^x$")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("y")
axs[1, 0].grid(True)

# 4 - f(x) = log(x+1)
axs[1, 1].plot(x_positive, y_log, color='m')
axs[1, 1].set_title(r"$f(x) = \log(x+1)$")
axs[1, 1].set_xlabel("x")
axs[1, 1].set_ylabel("y")
axs[1, 1].grid(True)

# Grafiklar orasidagi joyni moslash
plt.tight_layout()

# Grafikni ko‘rsatish
plt.show()