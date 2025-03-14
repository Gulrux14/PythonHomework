import numpy as np

# Custom function to calculate power
def custom_power(base, exponent):
    return base ** exponent  # Darajaga oshirish operatsiyasi

# Vectorizing the function
vectorized_power = np.vectorize(custom_power)

# Arrays of bases and exponents
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

# Calculating the power for each pair
results = vectorized_power(bases, exponents)

# Natijani chiqarish
print(list(results))