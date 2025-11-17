def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    if not mat:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("ragged matrix")
    
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("ragged matrix")
    
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("ragged matrix")
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]

if __name__ == "__main__":
    print("Testing transpose:")
    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
    print(transpose([[1, 2], [3, 4]]))
    print(transpose([]))
    
    print("\nTesting row_sums:")
    print(row_sums([[1, 2, 3], [4, 5, 6]]))
    print(row_sums([[-1, 1], [10, -10]]))
    print(row_sums([[0, 0], [0, 0]]))
    
    print("\nTesting col_sums:")
    print(col_sums([[1, 2, 3], [4, 5, 6]]))
    print(col_sums([[-1, 1], [10, -10]]))
    print(col_sums([[0, 0], [0, 0]]))
    
    print("\nTesting error cases:")
    try:
        transpose([[1, 2], [3]])
    except ValueError as e:
        print(f"Transpose error: {e}")
    
    try:
        row_sums([[1, 2], [3]])
    except ValueError as e:
        print(f"Row sums error: {e}")
    
    try:
        col_sums([[1, 2], [3]])
    except ValueError as e:
        print(f"Col sums error: {e}")