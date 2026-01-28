# TUPLES are ordered, immutable, can be of multiple data types and allow duplicate values.

fruits = ("apple", "orange", "mango", "banana")

# single element tuple

oneFruit = ("watermelon",)

# constructing a tuple

vegies = tuple(("aloo", "palak", "gobhi"))

# -----> most of the functions/methods/indexing/looping work like lists

# you can convert a tuple into list and c
"""
-> Add items
-> Remove items
"""

# unpacking a tuple: assigning the values of a tuple to variables

(fruit1, fruit2, fruit3, fruit4) = fruits

# using *

(red, orange, *yellow) = fruits

print(red)
print(orange)
print(yellow)

# you can multiply two tuples

print(fruits*2)