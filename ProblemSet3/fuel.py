def main():
    x, y = get_nums("Fraction: ")
    fuel = x/y * 100
    if fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(int(fuel), "%", sep="")

def get_nums(s):
    while True:
        try:
            exp = input(s)
            list = exp.split("/")
            x = int(list[0])
            y = int(list[1])
            if x > y or y <= 0 or x < 0:
                raise Exception()
            return x, y
        except:
            pass
    
main()