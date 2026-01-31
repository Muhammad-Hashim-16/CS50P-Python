def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    flag = True

    if s[0:2].isalpha(): # check1
        flag = True
    else:
        return False

    if len(s) <= 6: # check2
        flag = True
    else:
        return False

    count = 0
    for i in s: # check3
        if i.isalpha():
            count += 1
    if count < 2:
        return False
    else:
        flag = True

    if s.isalnum(): # check4
        flag = True   
    else:   
        return False

    index = s.find("0")
    check = s[:index]
    if check.isalpha():
        return False
    else:
        flag = True

    if s.isalpha(): #check6
        flag = True
    else:
        if s[-1:].isdigit():
            flag = True
        else:
            return False
        
    return flag


main()