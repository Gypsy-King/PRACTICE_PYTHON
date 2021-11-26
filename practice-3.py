# String methods

python = "Python is amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index) # = 5
index = python.index("n", index+1)
print(index)

print(python.find("Java")) # = -1
print(python.index("Java")) # error
print("hi") # it won't  be printed

print(python.count("n")) 

# String format

# Method 1
print("I am %d years old." % 20)
print("I like %s." % "Python")
print("Apple starts with %c." % "A")

# %s
print("I am %s years old." % 20)
print("My favorite color is %s and %s." % ("Blue","Red"))

# Method 2
print("I am {}years old.".format(20))
print("My favorite color is {} and {}.".format("Blue","Red"))
print("My favorite color is {0} and {1}.".format("Blue","Red"))
print("My favorite color is {1} and {0}.".format("Blue","Red"))

# Method 3
print("I am {age}years old, and my favorite color is {color}.".format(age = 20, color = "빨간"))
print("I am {age}years old, and my favorite color is {color}.".format(color = "빨간",age = 20))

# Method 4(over v3.6)
age = 20
color = "Red"
print(f"I am {age} years old, and my favorite color is {color}.")

# Escape Code
print("A picture is worth \n a thousand words")

print("I am 'coding'") or print('I am "coding"') or print("I am \"coding\"")

print("C:\\Users\\user\\Documents\\PRACTICE_PYTHON>") # to print \ we need \\

print("Red apple \r pine") # \r make cursor to front

print("Redd \b apple") # = backspace

print("Red \t apple") # = tab
