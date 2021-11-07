name = input("Type your name")
print("Welcome", name, "to this adventure!")

answer = input("you are in the dirt road it has come to an end  and you can go left or right? ").lower()

if answer == "left":
    print("You go along the forest")

elif answer == "right":
    print("You go along the forest")

else:
    print("Not a valid option. You loose.")

answer = input("The forest ends.  and you can go left or right? ").lower()

if answer == "left":
    print("You to the nearest hut")

elif answer == "right":
    print("you found a well")

else:
    print("Not a valid option. You loose.")