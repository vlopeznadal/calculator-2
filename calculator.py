"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
input_string = input("Enter your problem: ")
tokens = input_string.split(" ")
if tokens[0] == "q":
    quit
elif tokens[0] == 'add':
    print(add(float(tokens[1]), float(tokens[2])))