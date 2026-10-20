print("Welcome to the Hogwarts Sorting Hat")
trait = input("What best describes you? ").lower()

if trait == "brave":
    print("You belong in Gryffindor!")
    
elif trait == "intelligent":
    print("You belong in Ravenclaw!")
    
elif trait == "loyal":
    print("You belong in Hufflepuff!")
    
elif trait == "ambitious":
    print("You belong in Slytherin!")

elif trait == "didy":
    print("You belong in didyhouse!")

else:
    print("The Sorting Hat is confused.")