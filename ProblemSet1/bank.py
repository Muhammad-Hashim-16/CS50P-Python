greeting = input("Greeting: ").strip().lower()[:5]
lead = greeting[:1]

if greeting == "hello":
    print("$0.00")
elif lead == "H" or lead == "h":
    print("$20.00")
else:
    print("$100.00")