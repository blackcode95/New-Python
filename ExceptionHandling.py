#Exception Handling 

from unittest import result

from numpy import square

# try-except block

try:
    num = int(input("enter a integer: "))
    den = int(input("enter a integer: "))
    result = num/den
    print("Result = ", result)
except ZeroDivisionError:
    print(" Cannot divided by 0.")
except ValueError:
    print(" Invalid value is not satisfied.")
    
# try-except-else block 

try:
    a = int(input("enter a number: "))
except ValueError:
     print("invalid integer!!!!")
else:
    square = a ** 2
    print("Square of number is ", square)
    
# # try-except-finally block

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if 'file' in locals():
        file.close()