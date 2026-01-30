import random

def main():

    n = int(input("How many experiments do you wanna perform? "))
    head_C = 0
    tail_C = 0
    head_P = 0.0000
    tail_P = 0.0000
    count = 0
    flip = 0

    print("No of Experiments    Probability of H    Probability of T")

    for i in range(1, n):
        flip = random.randint(0, 1)
        if flip:
            head_C += 1
        else:
            tail_C += 1
        count += 1
        
        if i < 10:
            show(i, head_C, tail_C, count, 14)
        elif i < 100 and i%10 == 0:
            show(i, head_C, tail_C, count, 13)
        elif i < 1000 and i%100 == 0:
            show(i, head_C, tail_C, count, 12)
        elif i < 10000 and i%1000 == 0:
            show(i, head_C, tail_C, count, 11)
        elif i < 100000 and i%10000 == 0:
            show(i, head_C, tail_C, count, 10)
        elif i < 1000000 and i%100000 == 0:
            show(i, head_C, tail_C, count, 9)
        elif i < 10000000 and i%1000000 == 0:
            show(i, head_C, tail_C, count, 8)
        elif i < 100000000 and i%10000000 == 0:
            show(i, head_C, tail_C, count, 7)

    

def show(i, head_C, tail_C, count, spaces):
    head_P = format((head_C / count) * 100, ".4f")
    tail_P = format((tail_C / count) * 100, ".4f")
    print("  ", i, " " * spaces, "         ", head_P, "             ", tail_P, sep="")



main()