def main():
    time = input("What's the time? ")
    time = convert(time)
    
    if 7 <= time <= 8:
        print("Breakfast")
    elif 12 <= time <= 13:
        print("Lunch")
    elif 18 <= time <= 19:
        print("Dinner")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = float(hours + (minutes/60))
    return time


if __name__ == "__main__":
    main()