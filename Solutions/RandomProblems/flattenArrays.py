def flatten_one_depth(lst):
    """
    Flattens only one level of nesting.
    
    Parameters:
        lst (list): The input list which may contain nested lists.
        
    Returns:
        list: A new list with only one level of nesting removed.
    """
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    return flattened

# Example usage:
nested = [1, 2, 3, [4, 5, [6, 7, 8, 9]]]
print("One level flatten:", flatten_one_depth(nested))
# Output: [1, 2, 3, 4, 5, [6, 7, 8, 9]]
