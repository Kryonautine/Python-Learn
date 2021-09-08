# Defining Variables
side1 = int(input("Enter the 1st side of the triangle : \n"))
side2 = int(input("Enter the 2nd side of the triangle : \n"))
side3 = int(input("Enter the 3rd side of the triangle : \n"))

# Calculating Area by Heron's Formula
semiPerimeter = (side1 + side2 + side3) / 2
triangleArea = (
    semiPerimeter
    * (semiPerimeter - side1)
    * (semiPerimeter - side2)
    * (semiPerimeter - side3)
) ** 0.5

# Showing output to user
print("The Area of the triangle is : ", triangleArea)
