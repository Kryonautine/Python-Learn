order = int(input("Enter Order of square matrix : "))

matrix = []
row = []
for i in range(order):
    for j in range(order):
        print("Enter the (",i,",",j,") element : ")
        ele = int(input())
        row.append(ele)
    matrix.append(row)
    row = []

diagSum = 0
for i in range(order):
    diagSum = diagSum + matrix[i][i]

reverseSum = 0
for i in range(order):
    j = order - i - 1
    reverseSum = reverseSum + matrix[i][j]

print("The sum of diagonal elements is ",diagSum)
print("The sum of reverse diagonal elements is ",reverseSum)

print(matrix)
