## Integers

# You can add, subtract, mutiply, and divide
math = 2 + 3
print(math)
# For exponents, python using two ** symbols
math = 2 ** 3
print(math)
# You can also use order of operations
math = (2 + 3) * 4
print(math)

# Floats - python calls any number with a decimal point a float
# When you divide any two numbers, even if they are integers, you will get a float
math = 4/2
print(math)
# If you mix an integer and a float in any other operation, you'll get a float as well:
math = 1 + 2.0
print(math)
math = 2 * 3.0
print(math)
math = 3.0 ** 2
print(math)

# Underscores in Numbers
# When writing long numbers, you can group them with underscores to make them more readable
universe_age = 14_000_000_000
print(universe_age) # But, it will still print out as normal, python ignores them when storing it

# Multiple Assignment
# Example of initializing all these variables to zero
x, y, z = 0, 0, 0

# Constants
# Python does not have built-in constants, but python programmers use ALL CAPS to show it should be treated as a constant and never changed
MAX_CONNECTIONS = 5000

# 2-9: Number Eight
print(5+3)
print(16/2)
print(4*2)
print(10-2)

# 2-10: Favorite Number
favorite_number = 18
print(f"My favorite number is {favorite_number}!")