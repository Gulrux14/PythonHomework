import numpy as np

# Koeffitsiyentlar matritsasi
A = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

# Ozod hadlar vektori
B = np.array([12, -5, 15])

# Tenglamalar tizimini yechish
currents = np.linalg.solve(A, B)

# Natijani chiqarish
print(list(currents))