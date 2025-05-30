def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if the input is actually a list
    if not isinstance(lst, list):
        print("Error: First parameter must be a list")
        return lst
    
    # Go through each position in the list
    for i in range(len(lst)):
        # If the current item matches what we're looking for
        if lst[i] == find_val:
            # Replace it with the new value
            lst[i] = replace_val
    
    # Return the modified list
    return lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print("=== Testing find_and_replace function ===")
print()

# Test case 1: Replace 2 with 5 in [1, 2, 3, 4, 2, 2]
print("Test case 1: find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)")
original_list1 = [1, 2, 3, 4, 2, 2]
print(f"Original list: {original_list1}")
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(f"After replacing 2 with 5: {result1}")
print()

# Test case 2: Replace "apple" with "orange" in ["apple", "banana", "apple"]
print('Test case 2: find_and_replace(["apple", "banana", "apple"], "apple", "orange")')
original_list2 = ["apple", "banana", "apple"]
print(f"Original list: {original_list2}")
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(f'After replacing "apple" with "orange": {result2}')