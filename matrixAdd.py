def matrixInput(order):
    row = []
    matrix = []
    for i in range(order):
        for j in range(order):
            print("Enter element (", i, ", ", j, ") : ", end="")
            ele = int(input())
            row.append(ele)
        matrix.append(row)
        row = []
    return matrix

def matrixAdd(order,matrix1,matrix2):
    row = []
    matrixSum = []
    for i in range(order):
        for j in range(order):
            ele = matrix1[i][j] + matrix2[i][j]
            row.append(ele)
        matrixSum.append(row)
        row = []
    return matrixSum

def matrixDisplay(order,matrix):
    for i in range(order):
        for j in range(order):
            print(matrix[i][j], " ", end="")
        print()

# Defining Order of matrices and the matrices as lists

order = int(input("Enter the order of square matrices you wish to add : "))
matrix1 = []
matrix2 = []
matrixSum = []
row = []

# Taking in the elements of matrices 1 & 2

print("Enter the elements of the first matrix (left to right,top to bottom)")
matrix1 = matrixInput(order)

print("Enter the elements of the second matrix (left to right,top to bottom)")
matrix2 = matrixInput(order)

# Calculating their sum
matrixSum = matrixAdd(order,matrix1,matrix2)

# Displaying the matrices and their sum

for i in range(order):
    for j in range(order):
        print(matrix1[i][j], " ", end="")
    print()

print(" + ")

for i in range(order):
    for j in range(order):
        print(matrix2[i][j], " ", end="")
    print()

print(" = ")

for i in range(order):
    for j in range(order):
        print(matrixSum[i][j], " ", end="")
    print()

