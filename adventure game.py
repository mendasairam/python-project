print("Welcome to the Adventure Game!")
print("You find yourself at a crossroads in a dark forest.")
print("Do you want to go left or right?")

choice1 = input("Enter 'left' or 'right': ").lower()

if choice1 == "left":
    print("You head left and find a mysterious cave.")
    print("Do you want to enter the cave or keep walking?")
    
    choice2 = input("Enter 'enter' or 'walk': ").lower()
    
    if choice2 == "enter":
        print("Inside the cave, you discover a treasure chest!")
        print("Do you want to open the chest or leave it alone?")
        
        choice3 = input("Enter 'open' or 'leave': ").lower()
        
        if choice3 == "open":
            print("The chest is filled with gold and jewels. Congratulations, you are rich!")
        else:
            print("You leave the chest alone and exit the cave. You return home safely.")
            
    else:
        print("You keep walking and eventually find your way out of the forest. You are safe.")
        
elif choice1 == "right":
    print("You head right and come across a wild animal.")
    print("Do you want to fight the animal or run away?")
    
    choice2 = input("Enter 'fight' or 'run': ").lower()
    
    if choice2 == "fight":
        print("You fight the animal and win. You find a safe path out of the forest.")
    else:
        print("You run away and eventually find your way back home safely.")
        
else:
    print("You stand there indecisively until night falls. You are lost in the forest.")
