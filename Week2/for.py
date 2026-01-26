# for loop iterates over a sequence maybe list, tuple, dictionery, string or a set

# looping through a string
for x in "hashim":
    print(x)

# looping through a list
students = ["hashim", "moutasim", "kabeer"]
for student in students:
    print(student, "", end="")

# looping through a range | for (int i=0; i<5; i += 2) means same as range(0, 5, 2)
for i in range(1, 10, 2):
    print(i)

# else statement
for i in range(3):
    print(i)
else:
    print("Loop ended!")

# nested loops
for i in range(5):
    for j in range(1, i+2):
        print(j, "", end="")
    print()
    