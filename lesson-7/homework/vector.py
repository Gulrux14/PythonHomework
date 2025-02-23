import math

class Vector:
    def init(self, *components):
        self.components = components

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def sub(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def mul(self, other):
        if isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector):  # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication with type not supported.")

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[a / mag for a in self.components])

    def repr(self):
        return f"Vector{self.components}"