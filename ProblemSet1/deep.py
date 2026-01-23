answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.lower()

match answer:
    case "42" | "forty two" | "forty_two":
        print("Yes")
    case _:
        print("No")