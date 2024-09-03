# program for simple calculator and take input from user

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

print("select operation:-\n"
    "1. Addition\n"
    "2. Subtraction\n"
    "3. Multiplication\n"
    "4. Divison\n")

#taking input from user

a=float(input("Enter a:"))

selection=int(input("select arithematic operation:-"))

b=float(input("Enter b:"))

if selection==1:
    print(a,"+",b,"=",addition(a,b))

elif selection==2:
    print(a,"-",b"=",subtraction(a,b))

elif selection==3:
    print(a,"*",b,"=",multiplication(a,b))

elif selection==4:
    print(a,"/",b,"=",division(a,b))

else:
    print("INVALID INPUT")

