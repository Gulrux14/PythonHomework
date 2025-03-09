import numpy as np

# 10. Transpose of a 4x4 matrix
matrix_4x4 = np.random.randint(1, 10, (4, 4))
transpose_matrix = matrix_4x4.T
print("Original 4x4 Matrix:\n", matrix_4x4)
print("\nTransposed 4x4 Matrix:\n", transpose_matrix)

# 11. Determinant of a 3x3 matrix
matrix_3x3 = np.random.randint(1, 10, (3, 3))
determinant = np.linalg.det(matrix_3x3)
print("\nDeterminant of 3x3 Matrix:", determinant)

# 12. Matrix product of (3x4) and (4x3)
matrix_A = np.random.randint(1, 10, (3, 4))
matrix_B = np.random.randint(1, 10, (4, 3))
product_AB = np.dot(matrix_A, matrix_B)
print("\nMatrix Product of A(3x4) and B(4x3):\n", product_AB)

# 13. Matrix-vector multiplication
matrix_3x3 = np.random.randint(1, 10, (3, 3))
vector_3x1 = np.random.randint(1, 10, (3, 1))
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)
print("\nMatrix-Vector Product:\n", matrix_vector_product)

# 14. Solve Ax = b (linear system)
A = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 1))
x = np.linalg.solve(A, b)
print("\nSolution to Ax = b:\n", x)

# 15. Row-wise and Column-wise sum of a 5x5 matrix
matrix_5x5 = np.random.randint(1, 10, (5, 5))
row_sum = matrix_5x5.sum(axis=1)
col_sum = matrix_5x5.sum(axis=0)
print("\nRow-wise Sum:", row_sum)
print("Column-wise Sum:", col_sum)