def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # First, check if both inputs are numeric (integers or floats)
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        print("Error: Both inputs must be numeric")
        return False
    
    # Check if divisor is zero (can't divide by zero)
    if divisor == 0:
        print("Error: Cannot divide by zero")
        return False
    
    # Check if num is divisible by divisor
    # If the remainder is 0, then it's divisible
    if num % divisor == 0:
        return True
    else:
        return False

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print("=== Testing check_divisibility function ===")
print()

# Test case 1: 10, 2
print("Test case 1: check_divisibility(10, 2)")
result1 = check_divisibility(10, 2)
print(f"Result: {result1}")
print()

# Test case 2: 7, 3
print("Test case 2: check_divisibility(7, 3)")
result2 = check_divisibility(7, 3)
print(f"Result: {result2}")
print()

# Additional test to show error handling
print("Additional test: check_divisibility(10, 0)")
result3 = check_divisibility(10, 0)
print(f"Result: {result3}")