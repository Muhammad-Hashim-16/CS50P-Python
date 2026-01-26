camelText = input("Enter the variable name: ")

# prefferedNameCase

snakeText = ""

for l in camelText:
    if l.isupper():
        snakeText += "_" + l
    else:
        snakeText += l

print(snakeText.lower())