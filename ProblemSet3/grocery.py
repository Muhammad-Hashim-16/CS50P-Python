def main():
    shopping()


def shopping():
    cart = list(())
    while True:
        try:
            item = input().upper()
            cart.append(item)
        except EOFError:
            break
    cart.sort()
    cart_dict = dict()
    for x in cart:
        if x not in cart_dict:
            cart_dict[x] = 1
        else:
            cart_dict[x] += 1
    for x, y in cart_dict.items():
        print(y, x)


main()