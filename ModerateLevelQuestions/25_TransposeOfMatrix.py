# Function to transpose a matrix
def transpose(matrix):
    m = len(matrix)        # number of rows
    n = len(matrix[0])     # number of columns

    # Create an empty transpose matrix of size n x m
    t = [[0 for _ in range(m)] for _ in range(n)]

    # Fill transpose
    for i in range(m):
        for j in range(n):
            t[j][i] = matrix[i][j]

    return t


# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Get transpose
result = transpose(matrix)

# Print result
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTranspose:")
for row in result:
    print(row)


#Alternate Method 
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transpose)


#Output
#Original Matrix:
#[1, 2, 3]
#[4, 5, 6]

#Transposed Matrix:
#[1, 4]
#[2, 5]
#[3, 6]
