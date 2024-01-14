name = "Yash"
last = 'Arora'
# name="H" can`t

# String Concatenation
new_name = "Hi," + name
print(new_name)

#  String Repetition
print(" " + name * 3)

#  Accessing Character by Character
print(name[1])

#  Slicing
print(name[0:3])  # Yash, 3rd index excluded, from 0 onwards included.

#  String Length
print(len(name))

#  String Formatting
print("My Name is {0} {1}".format(name, last))

#  All String Methods below:
print(name + last)

print(len(name))

print(name[0])
print(name[0:3])

no = 3
fName = "yash arora"
print(str(no))

print(type(name))

print(name.upper())  # isupper() T or F
print(name.lower())  # islower() T or F
print(name.capitalize())
print(fName.title())

str = "abcda"
print(str.isalpha())  # True
str1 = "abc2"
print(str1.isalpha())  # False
print(str.isdigit())
print(str.startswith("a"))
print(str.endswith("a"))
print(fName.strip())

print(str.find("d"))  # index wise return first one which is found, return -1 if not found
# print(str.index("aa")) same as find() but raises an exception if not found.
print(str.replace("a", "o"))

print(f"My name is {name} {last}")
print("My name is {} {}".format(name, last))

split = fName.split(" ")
print(split)

