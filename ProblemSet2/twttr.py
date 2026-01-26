text = input("Enter: ")

vowels = "aeiouAEIOU"

returnText = ""

for c in text:
    if c not in vowels:
        returnText += c

print("Output:", returnText)