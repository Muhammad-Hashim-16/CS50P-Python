##### Read strings from w3schools. #####

name = str("Muhammad Hashim")
print(type(name)) # prints datatype
print(len(name)) # prints the length of string
print("Has" in name)
print("hashim" not in name)

# String slicing
print(name[3:6]) # last character is not included
print(name[:5])
print(name[10:])
print(name[-7:-1])

# String Methods
a = "  Hello, world!  "
print(a.upper())
print(a.lower())
print(a.strip()) # removes white spaces
print(a.replace("l", "k"))
print(a.split(",")) # splits on the base of ","

# String Formats
price = 60
text = f"This was the price: {price}." # the curly brackets can contain
                                       # any python code.
print(text)






