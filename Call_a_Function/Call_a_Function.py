# define a function that requires no arguments
def greet():
    print("Hello!")

# define a function with a few arguments
def multiply(a,b):
    c = int(a)*int(b)
    print(str(c))

# define a function with optional arguments
def message(a, b = None):
    print("a: " + str(a) + "\nb: " + str(b))
    return a
message(5)
message(5,6)

# call a function with named arguments
message(b = 5, a = 6)

# call a function with a variable number of arguments

# Using a function in statement context
message(multiply(5,6))
# Using a function in first-class context within an expression

# Obtaining the return value of a function

# Distinguishing built-in functions and user-defined functions

# Distinguishing subroutines and functions

# Stating whether arguments are passed by value or by reference

# Is partial application possible and how
