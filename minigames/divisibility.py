# Defining players
p1 = input("Player 1 is :")
p2 = input("Player 2 is :")
p3 = input("Player 3 is :")
p4 = input("Player 4 is :")
p5 = input("Player 5 is :")

# Entering number
no = int(input("Enter number here :"))

# Checking Divisibility
if no % 2 == 0:
    print(p1, "wins")

if no % 9 == 0 or no % 11 == 0:
    print(p2, "wins")
else:
    print(p5, "wins")

if no % 5 == 0:
    print(p3, "wins")

if no % 7 == 0:
    print(p4, "wins")
