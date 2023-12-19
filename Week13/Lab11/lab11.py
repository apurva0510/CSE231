import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
    
    def __str__(self): # returns a string representation of the vector
        return "({:.2f}, {:.2f})".format(self.x, self.y)

    def __repr__(self):
        return "({:.2f}, {:.2f})".format(self.x, self.y)
  
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == int:
            return Vector(self.x * other, self.y * other)
        elif type(other) == Vector:
            return round(self.x * other.x + self.y * other.y, 1)

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

    def unit(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot convert zero vector to a unit vector")
        self.x = self.x * (1 / magnitude)
        self.y = self.y * (1 / magnitude)


def main():
    # Test Vector class methods
    v1 = Vector(3, 4)
    v2 = Vector(5, 2)
    
    print("v1:", v1)
    print("v2:", v2)
    
    # Test __eq__ method
    print("v1 == v2:", v1 == v2)
    
    # Test __add__ method
    v3 = v1 + v2
    print("v1 + v2:", v3)
    
    # Test __sub__ method
    v4 = v1 - v2
    print("v1 - v2:", v4)
    
    # Test __mul__ method
    v5 = v1 * 2
    print("v1 * 2:", v5)
    
    v6 = v1 * v2
    print("v1 * v2:", v6)
    
    # Test magnitude method
    print("Magnitude of v1:", v1.magnitude())
    
    # Test unit method
    try:
        zero_vector = Vector()
        zero_vector.unit()
    except ValueError as e:
        print(str(e))
    

if __name__ == "__main__":
    main()