#Do the multiplication using the inheritance concept

class parentmultiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class childmultiply(parentmultiply):
    pass
    def multiply(self):
        return self.a * self.b

obj = childmultiply(50, 5)
print("Multiplication of a and b is:", obj.multiply())