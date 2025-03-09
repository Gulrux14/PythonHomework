import numpy as np

# 8. Multiply a 5x3 matrix by a 3x2 matrix
matrix_5x3 = np.random.randint(1, 10, (5, 3))
matrix_3x2 = np.random.randint(1, 10, (3, 2))
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("5x3 * 3x2 Matrix Product:\n", product_5x2)

# 9. Dot product of two 3x3 matrices
matrix_a = np.random.randint(1, 10, (3, 3))
matrix_b = np.random.randint(1, 10, (3, 3))
dot_product = np.dot(matrix_a, matrix_b)
print("\nDot Product of Two 3x3 Matrices:\n", dot_product)