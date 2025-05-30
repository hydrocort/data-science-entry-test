def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric (integers or floats)
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    
    # Swap the values using Python's tuple unpacking
    x, y = y, x
    
    # Print the swapped values
    print(f"Swapped values: x = {x}, y = {y}")
    
    return 

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Test case 1: "Apple", 10
print("Test case 1: swap('Apple', 10)")
result1 = swap("Apple", 10)
if result1 == -1:
    print("Error: One or both inputs are not numeric")
print()

# Test case 2: 9, 17
print("Test case 2: swap(9, 17)")
result2 = swap(9, 17)
if result2 == -1:
    print("Error: One or both inputs are not numeric")