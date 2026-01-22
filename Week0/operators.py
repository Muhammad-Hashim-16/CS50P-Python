x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

print(round(x+y))
print(round(x/y, 2))

# You can separate digits like this 1,000,000

z = x+y
print(f"{z:,}")

