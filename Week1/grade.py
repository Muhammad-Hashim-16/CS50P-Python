print("----------------- Grade Calculator -----------------")

score = int(input("What is your score? "))

if score > 100:
    print("Score greater than 100 is not possible.")
elif 90 <= score <= 100:
    print("Your grade is A+.")
elif 80 <= score < 90:
    print("Your grade is A.")
elif 70 <= score < 80:
    print("Your grade is B.")
elif 60 <= score < 70:
    print("Your grade is C.")
elif 50 <= score < 60:
    print("Your grade is D.")
elif 40 <= score < 50:
    print("Your grade is E.")
else:
    print("Your grade is F.")

# Even more optimized:

if score >= 90:
    print("Grade: A+.")
elif score >= 80:
    print("Grade: A.")
elif score >= 70:
    print("Grade: B.")
elif score >= 60:
    print("Grade: C.")
elif score >= 50:
    print("Grade: D.")
elif score >= 40:
    print("Grade: E.")
else:
    print("Grade: F")