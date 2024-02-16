from array import array

# Creating an array of integers
my_array = array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(my_array[0])  # Output: 1

# Appending
my_array.append(6)
print(my_array)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Iterating
for element in my_array:
    print(element)
