import math 

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiplay(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        try:
            return x/y
        except ZeroDivisionError:
            return "tivy 0-i chi bajanvum"
    
def power(x, y):
    return math.pow(x, y)
def squere_root(x, y):
    return math.sqrt(x, y)

num1 = float(input("Enter the first number: "))
sign = input("yntreq + - * / # ** ")
num2 = float(input("Enter the second number: "))

if sign == "+":
    print(add(num1, num2))
elif sign == "-":
    print(subtract(num1, num2))
elif sign == "*":
    print(multiplay(num1, num2))
elif sign == "/":
    print(divide(num1, num2))
elif sign == "**":
    print(power(num1, num2))
elif sign == "#":
    print(squere_root(num1, num2))