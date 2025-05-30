def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Start at the first position of the list (index 0)
    index = 0
    
    # Keep looping while we haven't reached the end of the list
    while index < len(lst):
        # Check if the current number is negative (less than 0)
        if lst[index] < 0:
            # We found the first negative number, so return it
            return lst[index]
        
        # Move to the next position in the list
        index += 1
    
    # We've checked all numbers and found no negatives
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print("=== Testing find_first_negative function ===")
print()

# Test case 1: List with negative numbers
print("Test case 1: find_first_negative([3, 5, -1, 7, -2, 8])")
test_list1 = [3, 5, -1, 7, -2, 8]
print(f"Original list: {test_list1}")
result1 = find_first_negative(test_list1)
print(f"First negative number: {result1}")
print()

# Test case 2: List with no negative numbers
print("Test case 2: find_first_negative([2, 10, 7, 0])")
test_list2 = [2, 10, 7, 0]
print(f"Original list: {test_list2}")
result2 = find_first_negative(test_list2)
print(f"First negative number: {result2}")