
# function()

def add(a, b):
    # Check if both arguments are of the same type
    if type(a) == type(b):
        # If both are numbers (int or float), add them directly
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        # If both are lists, concatenate them
        elif isinstance(a, list) and isinstance(b, list):
            return a + b
        # If both are strings, concatenate them
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("Unsupported types for add function")
    else:
        raise TypeError("a and b must be of the same type")

# Examples:
print(add(5, 3))        # Output: 8
print(add(5.0, 3.2))    # Output: 8.2
print(add("hello", "world")) # Output: "helloworld"
print(add([1, 2], [3, 4]))   # Output: [1, 2, 3, 4]

