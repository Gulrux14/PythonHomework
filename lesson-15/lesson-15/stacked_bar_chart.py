import numpy as np
import matplotlib.pyplot as plt

# Vaqt oralig'lari
time_periods = ['T1', 'T2', 'T3', 'T4']

# Har bir kategoriya bo'yicha qiymatlar
category_A = [10, 15, 20, 25]
category_B = [5, 10, 15, 20]
category_C = [8, 12, 18, 22]

# Ranglar
colors = ['blue', 'green', 'red']

# Grafik chizish
plt.figure(figsize=(8, 6))

# To‘plangan ustunlar
plt.bar(time_periods, category_A, color=colors[0], label='Category A')
plt.bar(time_periods, category_B, color=colors[1], bottom=category_A, label='Category B')
plt.bar(time_periods, category_C, color=colors[2], bottom=np.array(category_A) + np.array(category_B), label='Category C')

# Sarlavha va o‘qlar
plt.title("Stacked Bar Chart: Categories over Time")
plt.xlabel("Time Periods")
plt.ylabel("Values")

# Legend (kategoriya nomlari)
plt.legend()

# Grid qo‘shish
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Grafikni ko‘rsatish
plt.show()