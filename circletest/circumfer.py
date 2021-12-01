def calcircum(radius):
    circumference = 2 * 3.14 * radius
    return circumference

def calarea(radius):
    area = 3.14 * (radius ** 2)
    return area

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle : "))
    circumference = calcircum(radius)
    print("The circumference of the circle is : ",circumference)
