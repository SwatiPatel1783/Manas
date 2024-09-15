#Do the division using the class concept

class division():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def divide(self):
       return self.x / self.y


obj = division(30,15)
print("division of x and y is : ", obj.divide())
