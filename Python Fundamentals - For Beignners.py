#Python 

import select


print("Hello ji😉")

#Variable

def hello():
    a = 10
    print(a)
    return
hello()

#Calculator 

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("Please select operation\n" 
      " 1. Add \n"
      " 2. Sub \n"
      " 3. Mul \n"
      " 4. Div \n")

select = int(input(" Select opertaion from 🔢. "))
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))

if select == 1:
    print(n1 , "➕ ", n2 , "= ", add(n1,n2))
    
elif select == 2:
    print(n1 , "➖ ", n2 , "= ", sub(n1,n2))
    
elif select == 3:
    print(n1 , "✖️ ", n2 , "= ", mul(n1,n2))
    
elif select == 4:
    print(n1 , "➗ ", n2 , "= ", div(n1,n2))
    
else:
    print("Invalid Operation! ")
