
A = [[0, 0, 0], 
     [0, 0, 0], 
     [0, 0, 0]]

def output(matrix):
    print(f"""{matrix[0]}
{matrix[1]} 
{matrix[2]}""")

output(A)

for x in range(0, 3):
    for y in range(0, 3):
        value = input("Enter value: ")
        A[x][y] = int(value)
        # print(A)

print(f"""
Original: 
{A[0]}
{A[1]}
{A[2]}
""")


# A = [[1, 2, 3], 
#      [4, 5, 6], 
#      [7, 8, 9]]

# In accordance with algorithm notes:

yellow = [1, 1, 1, 0, 0, 0, 0, 0, 0]
blue   = [1, 0, 0, 1, 0, 0, 1, 0, 0]
red    = [2, 2, 2, 2, 2, 2, 1, 1, 1]
green  = [2, 2, 1, 2, 2, 1, 2, 2, 1]

minor = [[0, 0, 0],
         [0, 0, 0], 
         [0, 0, 0]]


i = 0
while i < 9:
    # print(i%3)
    value = (A[yellow[i]][blue[i]] * A[red[i]][green[i]]) - (A[yellow[i]][green[i]] * A[red[i]][blue[i]])
    # print(f"({(A[yellow[i]][blue[i]] * A[red[i]][green[i]])- A[yellow[i]][green[i]] * A[red[i]][blue[i]]})")

    if i < 3:
        minor[0][(i%3)] = value
    elif i < 6:
        minor[1][i%3] = value
    else:
        minor[2][i%3] = value
    # print(minor)
    i += 1

print(f"""
Minor: 
{minor[0]}
{minor[1]}
{minor[2]}
""")
    
'''
Cofactor Operation Map:
[+, -, +]
[-, +, -]
[+, -, +]
'''

CF = minor

indices_to_negate = [(0, 1), (1, 0), (1, 2), (2, 1)]
for i, j in indices_to_negate:
    CF[i][j] = minor[i][j] * -1

print(f"""
Cofactor: 
{CF[0]}
{CF[1]}
{CF[2]}
""")

determinant = (A[0][0] * CF[0][0])+(A[0][1] * CF[0][1])+(A[0][2]*CF[0][2])
print(determinant)

inverseMatrix = [list(row) for row in zip(*minor)]

print(f"""
Inverse: 
    {inverseMatrix[0]}
1/{determinant}{inverseMatrix[1]}
    {inverseMatrix[2]}
""")










