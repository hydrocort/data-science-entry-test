def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists in the dictionary
    if key in dct:
        # Print the original value before updating
        print(f"Original value for '{key}': {dct[key]}")
    
    # Update the dictionary with the new key-value pair
    dct[key] = value
    
    # Return the updated dictionary
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# Test case 1: Empty dictionary, add new key "name" with value "Alice"
print("Test case 1: update_dictionary({}, 'name', 'Alice')")
result1 = update_dictionary({}, "name", "Alice")
print(f"Result: {result1}")
print()

# Test case 2: Dictionary with existing key "age", update its value
print("Test case 2: update_dictionary({'age': 25}, 'age', 26)")
result2 = update_dictionary({"age": 25}, "age", 26)
print(f"Result: {result2}")