def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if the input is actually a string
    if not isinstance(s, str):
        print("Error: Input must be a string")
        return s
    
    # Reverse the string using Python's slicing feature
    # [start:stop:step] where step=-1 means go backwards
    reversed_string = s[::-1]
    
    # Return the reversed string
    return reversed_string

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print("=== Testing string_reverse function ===")
print()

# Test case 1: "Hello World"
print('Test case 1: string_reverse("Hello World")')
original1 = "Hello World"
result1 = string_reverse("Hello World")
print(f'Original: "{original1}"')
print(f'Reversed: "{result1}"')
print()

# Test case 2: "Python"
print('Test case 2: string_reverse("Python")')
original2 = "Python"
result2 = string_reverse("Python")
print(f'Original: "{original2}"')
print(f'Reversed: "{result2}"')