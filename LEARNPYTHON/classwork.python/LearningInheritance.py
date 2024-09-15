# parent and child relationship is known as inheritance
# we can access the parent class property in child class

class parent():
    def parent_function(self):
        print("It is a parent function")


class child(parent):
    def child_function(self):
        print("It is an child function of child class")


obj = child()
obj.parent_function()
obj.child_function()
