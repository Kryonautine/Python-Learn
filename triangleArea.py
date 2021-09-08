# Heron's Formula
def heronsFormula():

    ## Defining Variables
    side1 = float(input("Enter the 1st side of the triangle : \n"))
    side2 = float(input("Enter the 2nd side of the triangle : \n"))
    side3 = float(input("Enter the 3rd side of the triangle : \n"))

    ## Calculating Area by Heron's Formula
    semiPerimeter = (side1 + side2 + side3) / 2
    triangleArea = (
        semiPerimeter
        * (semiPerimeter - side1)
        * (semiPerimeter - side2)
        * (semiPerimeter - side3)
    ) ** 0.5

    return triangleArea


# Base-Height Formula
def baseHeight():

    ## Defining Variables
    triangleBase = float(input("Enter the base of the triangle : \n"))
    triangleHeight = float(input("Enter the height of the triangle : \n"))

    ##Calculating Area
    triangleArea = (triangleBase * triangleHeight) / 2

    return triangleArea


if __name__ == "__main__":
    # Choosing Formula
    print("Welcome to the triangle area calculator. Choose a formula.")
    choice = 0

    while choice != 1 and choice != 2:
        choice = float(
            input("Enter 1 for Heron's Formula or 2 for Base-Height formula : \n")
        )

        if choice == 1:
            triangleArea = heronsFormula()

        elif choice == 2:
            triangleArea = baseHeight()

        else:
            print("Please enter a valid option.")

    # Showing output to user
    print("The Area of the triangle is : ", triangleArea)
