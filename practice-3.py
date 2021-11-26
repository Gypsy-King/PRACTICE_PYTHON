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