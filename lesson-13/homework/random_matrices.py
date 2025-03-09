import numpy as np

# 4. 3x3x3 Array with random values
array_3x3x3 = np.random.random((3, 3, 3))
print("3x3x3 Random Array:\n", array_3x3x3)

# 5. 10x10 Array with random values and min/max
array_10x10 = np.random.random((10, 10))
min_val = array_10x10.min()
max_val = array_10x10.max()
print("\n10x10 Random Array Min:", min_val, "Max:", max_val)

# 6. Random vector of size 30 and its mean
vector_30 = np.random.random(30)
mean_value = vector_30.mean()
print("\nMean of 30-element Vector:", mean_value)

# 7. Normalize a 5x5 random matrix
matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())
print("\nNormalized 5x5 Matrix:\n", normalized_matrix)