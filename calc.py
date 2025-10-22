from unittest import case

print("This is a calculator!")
print("You can add, subtract, multiply, divide numbers and find the modulus!")
print("Use add for addition\nsub for substraction\nmultiply for multiplication\ndivide for division\nmod for modulus")
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
def mod(x, y):
    return x % y
print("Write your operator here:")
x = input()
match x:
    case 'add':
        print(add(input(), input()))
    case 'sub':
        print(sub(input(), input()))
    case 'multiply':
        print(mul(input(), input()))
    case 'multiply':
        print(mul(input(), input()))
    case 'divide':
        print(div(input(), input()))
    case 'mod':
        print(mod(input(), input()))
