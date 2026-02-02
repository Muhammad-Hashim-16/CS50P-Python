def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    flag = True

    if not (2 <= len(s) <= 6): # check1
        return False

    if not s[0:2].isalpha(): # check2
        return False
    
    if not s.isalnum(): # check3
        return False

    for i in range(len(s)): 
        if s[i].isdigit():
            if s[i] == "0":
                return False
            if not s[i:].isdigit():
                return False
            break
        
    return flag


main()