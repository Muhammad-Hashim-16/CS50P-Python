# SETS are unordered, immutable, unindexed, contains distinct elements and of any data type.

setA = {"Batool", "Hashim", "Moutasim", "Zain"}

# constructing a set

setB = set((1, 2, 3, 4, 5))

# once a set is created, you can't change it's items but you can add newer

setB.add(10)

# update(): add a set(or any other data structure) into another one

setC = {"Azzam"}
setC.update(setA)

print(setA)

# to remove item(s) from set

setC.remove("Hashim") # if the item doesn't exist, it will cause an error
setC.discard("Zain") # if the item doesn't exist, it won't cause an error
setC.pop() # sets are unordered so you might not know ke which item gets deleted

setC.clear() # empties a set
del setC # completely deletes a set

### Set Operations ###

""" Summary

union()                       update()                          |
intersection()                intersection_update ()            &
difference()                  difference_update()               -
symmetric_difference()        symmetric_difference_update()     ^        ### keeps the elements that are not present in both
     |                                |                         :
     |                                |                         :
(stored in another set        (changes added to 1st set      (can't be used 
 can be used with other        can be used with other         with other data
 data structurs too.)          data structurestoo.)           structures.)

"""

set1 = {1, 2, 3, 4, 5}
set2 = {3, 5, 7}

set3 = set1.union(set2)
set1.update(set2)
set4 = set1 | set2

### Frozen Set ###

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))