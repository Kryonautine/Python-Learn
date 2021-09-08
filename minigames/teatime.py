# Choosing a name and defining variables
playnm = input("Choose a name : ")
choice1 = "a"
choice2 = "a"

# Scenario 1
while choice1 != "tea" and choice1 != "coffee":
    choice1 = input(
        "You enter the house of Ms.Stachy Collins. She asks if you want tea or coffee.\nWhich beverage do you prefer?\n"
    ).lower()

# Scenario 2
while choice2 != "chips" and choice2 != "biscuits":
    choice2 = input(
        "Would you like some biscuits?, asks the lady.\n"
        "You see a glimpse of a packet of chips behind a drawer."
        "She offers you some biscuits.\nWhich do you choose, Chips or Biscuits?\n"
    ).lower()

# Possible Futures
if choice1 == "tea" and choice2 == "biscuits":
    print(
        "You sit down and enjoy a nice tea evening with the lady, talking about the new store down the street."
    )

elif choice1 == "tea" and choice2 == "chips":
    print(
        "She remarks at your poor choice of taste but nonetheless chats with you amicably."
    )

elif choice1 == "coffee" and choice2 == "biscuits":
    print(
        "She looks at you, visibly disgusted at a person who prefers coffee over tea, but nonetheless apologises for her dog eating your diploma."
    )

elif choice1 == "coffee" and choice2 == "chips":
    print(
        "She is horrified at your choice of a snack and refuses to accept or help you to regain your diploma after her dog tore it to shreds."
    )
