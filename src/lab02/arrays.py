def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
   
    if not nums:
        raise ValueError("Cannot find min/max of empty list")
    
    min_val = nums[0]
    max_val = nums[0]
    
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return (min_val, max_val)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))


def flatten(matrix: list[list | tuple]) -> list:
    result = []
    
    for item in matrix:
        if not isinstance(item, (list, tuple)):
            raise TypeError("All elements must be lists or tuples")

        result.extend(item)
    
    return result


#testirovanje
if __name__ == "__main__":
    print("Testing min_max:")
    print(min_max([3, -1, 5, 5, 0]))  
    print(min_max([42])) 
    print(min_max([-5, -2, -9]))  
    print(min_max([1.5, 2, 2.0, -3.1]))  

    print("\nTesting unique_sorted:")
    print(unique_sorted([3, 1, 2, 1, 3]))  
    print(unique_sorted([])) 
    print(unique_sorted([-1, -1, 0, 2, 2]))  
    print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) 
    
    print("\nTesting flatten:")
    print(flatten([[1, 2], [3, 4]])) 
    print(flatten([[1, 2], (3, 4, 5)]))
    print(flatten([[1], [], [2, 3]]))  
 
    print("\nTesting error cases:")
    try:
        min_max([])
    except ValueError as e:
        print(f"min_max empty list: {e}")
    
    try:
        flatten([[1, 2], "ab"])
    except TypeError as e:
        print(f"flatten with string: {e}")