# The TRY block lets you test a block of code for errors.
# The ESCEPT block lets you handle the error.
# The ELSE block lets you execute code when there is no error.
# The FINALLY block lets you execute code, regardless of the result of the try- and except blocks.

def main():
    print(get_int())

def get_int():
    while True:
        try:
            return int(input("Enter a number: "))
        except:
            return get_int()
            # pass

main()