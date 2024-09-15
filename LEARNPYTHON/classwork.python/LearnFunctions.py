# can give any name of function

# argument function: if input is changed then code should not be changed
def argument_function(name, age):
    print(name, age)


argument_function("Shreyans", 40)


# no argument method: when only we need to perform the click action
def no_argument_function():
    print("This is no argument function")


no_argument_function()


#return type function: one function's output should be an input of another function
def return_type_fucntion():
    a = 20
    return a

def substraction():
    c = 30-return_type_fucntion()
    print(c)
substraction()


# no return type function
def no_return_type_function():
    print("This is no return type function")

no_return_type_function()