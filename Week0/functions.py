print("5+5")
print("Hello, world!") 
# Hello, world! is the side effect (the outcome of a function.)
# A side effect maybe an alert, a return value etc.
# Computer's gonna take you literally.

"""
Anything between this is a comment.
"""

# Same style goes for multi line strings.

goal = input("What is your goal? ")
print("You want to become a", goal, ".") # These are 3 arguments.
print("You want to become a " + goal + ".") # This is 1 argument.
# The return value of input function can be stored in a variable.

print(f"My goal is becoming a {goal} too.") # String Format

print("You are", input("What is your name? "))

# User def functions
def hello():
    print("hello, world")

hello()


