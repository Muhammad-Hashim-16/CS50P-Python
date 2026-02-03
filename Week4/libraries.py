import sys
print("My name is ", end="")
for arg in sys.argv:
    print(arg + " ", end="")