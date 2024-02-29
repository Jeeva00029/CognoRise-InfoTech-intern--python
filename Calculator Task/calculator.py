"""
Basic Calculator application
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Square
6.Square Root
7.Factorial
8.Logarithm
9.Quit
"""
def additon(a,b):
    print("The Addition of ",a,"and ",b,"is",a+b)

def substraction(a,b):
    print("The Subtraction of ", a, "and ", b, "is", a - b)

def multiply(a,b):
    print("The Multiplication of ", a, "and ", b, "is", a * b)

def division(a,b):
    print("The Division of ", a, "and ", b, "is", a / b)

def square(a):
    print("The Square of ",a,"is",a*a)

def squareroot(a):
    import math
    print("The Squareroot of ",a,"is",math.sqrt(a))

def factorial(a):
    import math
    print("The Factorial of ",a,"is",math.factorial(a))

def logorithm(a,b):
    import math
    print("The Logarthm of ",a,"is",math.log(a,b))

def exit():
    quit()

print("********************BASIC ARITHMETIC CALCULATOR********************* ")
while True:
    print(".......................................................................................")
    print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Square \n 6.Square Root \n 7.Factorial \n 8.Logarithm \n 9.Quit")
    print(".......................................................................................")
    choice=int(input("Enter the choice:"))
    if(choice>0 and choice<=9):
        if(choice==1):
            a=float(input("Enter the Number_1:"))
            b=float(input("Enter the Number_2:"))
            additon(a,b)
        elif(choice==2):
            a = float(input("Enter the Number_1:"))
            b = float(input("Enter the Number_2:"))
            substraction(a,b)
        elif(choice==3):
            a = float(input("Enter the Number_1:"))
            b = float(input("Enter the Number_2:"))
            multiply(a,b)
        elif(choice==4):
            a = float(input("Enter the Number_1:"))
            b = float(input("Enter the Number_2:"))
            division(a,b)
        elif(choice==5):
            a = float(input("Enter the Number:"))
            square(a)
        elif(choice==6):
            a=float(input("Enter the Number:"))
            squareroot(a)
        elif(choice==7):
            a=int(input("Enter the Number:"))
            factorial(a)
        elif(choice==8):
            a=float(input("Enter the Number:"))
            b=int(input("Enter the Base Number:"))
            logorithm(a,b)
        else:
            print("I hope is useful for you......\nTHANK YOU")
            break

    else:
        print("Invalid input")
        print("----------------------------------------------------------------------------------------")












