import numpy as np

# Koeffitsiyentlar matritsasi
A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])

# Ozod hadlar vektori
B = np.array([7, 4, 5])

# Tenglamalar tizimini yechish
solution = np.linalg.solve(A, B)

# Natijani chiqarish
print(list(solution))