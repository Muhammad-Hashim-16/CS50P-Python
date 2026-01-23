x = int(input("What is x? "))
y = int(input("What is y? "))

print()

if x > y:
    print("x is greater than y.")
elif x < y:
    print("x is smaller than y.")
else:
    print("x is equal to y.")

print()

if x < y or x > y:
    print("x is not equal to y.")
else:
    print("x is equal to y.")

print()

if x < y and x == y:
    print("x is less than or equal to y.")
else:
    print("x is not less than or equal to y.")

print()