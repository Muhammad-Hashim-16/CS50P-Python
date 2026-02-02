amountDue = 50
changeOwed = 0
total = 0

allowed = [5, 10, 25]

while True:
    coinInserted = int(input("Insert a coin: "))
    if coinInserted not in allowed:
        continue
    total += coinInserted
    if total >= 50:
        changeOwed = total - 50
        print("Here's you Coke!")
        print("Change:", changeOwed)
        break
    amountDue = 50 - total
    print("Amount due:", amountDue)