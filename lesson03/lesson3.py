# Lesson 3
# Maximum square side length based on input

# input
tiles = input("Enter the number of tiles: ")
# input() always a string
tiles = int(tiles)

# square root is exponent of a half
calculation = int((tiles ** 0.5) // 1)
# can also import math module, import math; calculations = math.sqrt(tiles)

print(f"The maximum side length is {calculation}")

.