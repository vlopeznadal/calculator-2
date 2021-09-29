"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter your problem: ")
    tokens = input_string.split(" ")
    if tokens[0] == "q":
        break
    elif tokens[1] == '+':
        print(add(float(tokens[0]), float(tokens[2])))
    elif tokens[1] == '-':
        print(subtract(float(tokens[0]), float(tokens[2])))
    elif tokens[1] == '*':
        print(multiply(float(tokens[0]),float(tokens[2])))
    elif tokens[1] == '/':
        print(divide(float(tokens[0]),float(tokens[2]))) 
    elif tokens[1] == 'square':
        print(square(float(tokens[0])))
    elif tokens[1] =='cube':
        print(cube(float(tokens[0])))
    elif tokens[1] == 'pow':
        print(power(float(tokens[0]), float(tokens[2])))
    elif tokens[1] == 'mod':
        print(mod(float(tokens[0]), float(tokens[2])))