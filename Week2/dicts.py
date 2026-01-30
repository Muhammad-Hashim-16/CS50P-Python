# # DICTIONERIES are ordered, mutable, contain key-value pairs and do not allow duplicates

# student = {
#     "name" : "Hashim",
#     "semester" : 2,
#     "gpa" : 3.71,
# }
# print(student)

# # accessing a single value

# print(student["name"])
# print(student.get("name"))

# # duplicates will overwrite existing values

# # length function gives the number of keys

# print(len(student))

# # constructing a dict

# car = dict(company = "Honda", model = "Civic", year = 2024)
# print(car)

# # the keys function (gives the list of all the keys)

# carKeys = car.keys()
# car["color"] = "White"
# print(carKeys)

# # the values function (gives the list of all the values)

# carValues = car.values()
# car["engine"] = "1.8L"
# print(carValues)

# # items() funtion will return each item in a dictionery as tuples in a list

# print(car.items())

# ## if you make a change or add a new item both the keys and the values list get updated

# # check if a specified key is present or not in a dict

# if"model" in car:
#     print("Yes!")

# # Add or update any value 

# car.update({"model" : 2025})

# # remove an item by pop() or the last inserted item by popitem()

# student.pop("gpa")
# student.popitem()

# # empty a dict by clear() or delete it by del

# student.clear()
# del car["model"]
# del student

# # Looping through a dict

# for x in car:
#     print(x) # gives keys
# for x in car.values():
#     print(x) # gives values
# for x in car.keys():
#     print(x) # gives keys
# for x, y in car.items():
#     print(x, y, sep=" : ") # gives keys, values

# # copying a dict

# car_2 = car.copy()
# car_3 = dict(car)

### Nested Dicts ###

myfamily = {
    "mama" : {"name" : "Bushra", "age" : 46},
    "papa" : {"name" : "Naeem", "age" : 47},
    "mai" : {"name" : "Hashim", "age" : 19},
    "bhai" : {"name" : "Huzaifa", "age" : 13}
}

# you can also make child dicts and add them to a parent dict

# accessing the items of a nested dict

for x, value in myfamily.items():
    print(x)
    for y in value:
        print(y, value[y], sep=" : ")
    print()