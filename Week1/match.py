letter = int(input("Enter a number from 1 to 5: "))

match letter:
    case 1:
        print("A")
    case 2:
        print("B")
    case 3:
        print("C")
    case 4:
        print("D")
    case 5:
        print("E")
    case _:
        print("?")

match letter:
    case 1 | 3 | 5:
        print("Odd")
    case 2 | 4:
        print("Even")
    case _:
        print("?")