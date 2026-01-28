# LISTS are ordered, mutable, and allow multiple items.

fruits = ["apple", "banana", "mango"]
print(fruits)

# length function

print(len(fruits))

# a list can also have different datatypes

multiple = [4, "string", False, "char", "bool"]
print(multiple)

# type of a list is literally 'list'

print(type(multiple))

# constructing a list

newList = list((1, 2, 3, 4))
print(newList)

# negative indexing

print(newList[-2])

# range of indexes (returns a new list)

print(newList[1:4])

# range of negative indexes (fzool cheez hai)

print(newList[-4:-1])

# checking if an item is present in a list or not

if "mango" in fruits:
    print("Yes mango is present.")
if "100" not in fruits:
    print(True)

# you can change a range of values (If you insert more items than you replace,
# the new items will be inserted where you specified, and the remaining items
# will move accordingly. Same goes for less items inserted.)

newList[1:4] = [3, 5, 7]

# the insert function

fruits.insert(2, "grapes")

# the append function (adds an item at the last)

fruits.append("orange")

# the extend function (to append another list, or any other collection - tuple, set or dict.)

newList.extend([9, 11])

# the remove funciton (removes a specified item)

fruits.remove("apple")

# the pop function (removes item of a certain index)

multiple.pop(4)

# del keyword (deletes a specific index or the whole list)

del multiple[3]

# the clear function (empties the list)

multiple.clear()

# looping through a list

for x in fruits:
    print(x)
for i in range(len(fruits)):
    print(fruits[i])

[print(x) for x in fruits] # Pythonic Expression

# list comprehension (or Pythonic Expression)

[print(f) for f in fruits if "g" not in f]
[print(i) for i in range(5)]
capitalFruits = [f.upper() for f in fruits]

print()

### Sorting lists in Python ###

vegies = ["aloo", "Palak", "gobhi", "gajar"]
vegies.sort()

# for descending order sorting

vegies.sort(reverse = True)

# sorting on the basis of how close the number is to let's say 50

def myFunc(n):
    return abs(n-50)

numbers = [100, 50, 65, 82, 23]
numbers.sort(key = myFunc)

# sort() is case sensitive, you can make it case insensitive like this

vegies.sort(key = str.lower)
print(vegies)

# reverse() can be used to reverse the current order of sorting

numbers.reverse()

### Joining lists in Python ###

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 +list2 # by adding

for x in list1:
    list2.append(x)

list1.extend(list2)