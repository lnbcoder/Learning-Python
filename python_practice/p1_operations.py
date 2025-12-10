# String Operations
name, surname, age = "Loveness", "Baloyi", 23

# Concatination of strings
print("Name: " + name + "\nSurname: " + surname)

# using f.strings
print(f"Name: {name} \nAge: {age}")

# using .format()
print("Name: {} \nAge: {}".format(name, age))

s = "God Loves You   "
print(f"Find: {s.find("o")}")
print(f"Count: {s.count("o")}")
print("Replace: " + s.replace("You","Us"))
print(f"Split: {s.split(" ")}")
print("Uppercase: " + s.upper())
print("Lowercase: " + s.lower())
print("Caplitalize every first letter in a paragraph: " + s.title())
print("Caplitalize first letter: " + s.capitalize())

letters = ['a','b','c']
print("Join: " + "-".join(letters))

word = "  Whitespace  "
print(word.strip())
print(word.rstrip())
print(word.lstrip())

# Arithmetic Operations
a, b = 10, 3

print(a + b)  # Addition
print(a - b)  # Subtraction 
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division
print(a % b)  # Modulus
print(a ** b) # Exponent

# Mathematical Functions using math module
# you will need to import math
import math

print(math.sqrt(25))  # square root
print(math.pow(3, 2)) # power

# Rounding Functions
pie_value = 3.14159
print(round(pie_value, 2))   # round off to two decimal place
print(math.floor(pie_value)) # round off to the nearest low value
print(math.ceil(pie_value))  # round off to the nearest high value

# Type Conversion
int(3.9)
float(5)
str(10)

# Assignment Operator: +=, -=, *=, /=
