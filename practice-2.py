# Simple equation
print(2 + 3 * 4) # = 14
print((2 + 3) * 4) # = 20

number = 2 + 3 * 3 # = 14
print(number)

number = number + 2 # = 16
print(number) # = 16

number += 2  # = 18
print(number) 

number *= 2 # = 36

number /= 2 # = 18

number -= 2 # = 16

number %= 5 # = 1

# math functions

print(abs(-5))				# 5(absolute value)
print(pow(4, 2))			# 4^2 = 4*4 = 16(square value)
print(max(5, 12))			# 12(maximun value between numbers)
print(min(5, 12))			# 5(minimun value between numbers)
print(round(3.14))			# 3
print(round(4.99))			# 5

from math import * # use all functions in math library
print(floor(4.99)) # = 4 (round up)
print(ceil(3.14)) # = 4 (round off)
print(sqrt(16)) # = 4 (square root)

# random functions
from random import *

print(random()) # generate random value between 0.0<= ~ <1.0
print(random()*10) # generate random value between 0.0<= ~ <10.0
print(int(random()*10)) # generate random value between 0<= ~ <10
print(int(random()*10 + 1)) # generate random value between 1<= ~ <=10

print(int(random()*45) + 1) *6 # generate random value between 1<= ~ <=45  # Korean loterry
print(randrange(1, 46)) # generate random value between 1< ~ <45
print(randint(1,45)) # generate random value between 1< ~ <45

# String
sentance = 'I am a boy'
print(sentance)
sentance2 = "Python is eaasy"
print(sentance2)
sentance3 = """I am a boy and
Python is eaasy
"""
print(sentance3) # use 3 single quotation it covers many sentances at once

# slicing
RRN = "900120-1234567"

print("sex : " + RRN[7])
print("birth year : " + RRN[0:2])
print("birth month : " + RRN[2:4])
print("birth day : " + RRN[4:6])

print("birth: " + RRN[:6])
print("back nums : " + RRN[7:])
print("back nums(start from the back) : " + RRN[-7:]) 