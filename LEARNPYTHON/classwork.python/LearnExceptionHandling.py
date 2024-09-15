# except block execute only when error occured in try block
# finally block execute each time
# try block can be written into the function and class
# if there is a no function or class then we can write directly 

try:
    a = int(input("Please enter the first number= "))
    b = int(input("Please enter the second number= "))
    c = a/b
    print(c)
except:
    print("Divide by zero is not possible")
finally:
    print("File close code should be written here ")

