             


def outputMatrix(matrix):
    print(f"""{matrix[0]}
{matrix[1]}""")
    
def inverse(matrix):
    det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])

    # Swapping
    temp = matrix [0][0] 
    matrix[0][0] = matrix[1][1]
    matrix[1][1] = temp

    # *-1 of other values
    matrix[0][1] *= -1
    matrix[1][0] *= -1
    
    inverse_matrix = f"""
1/{det} {matrix[0]}
     {matrix[1]}
    """
    return inverse_matrix


matrix = [[1, 5], 
          [3, 6]]

outputMatrix(matrix)
newMatrix = print(inverse(matrix))




