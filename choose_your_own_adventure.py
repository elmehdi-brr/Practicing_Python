name = input("Tyoe your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right)? ").lower()


if answer == "left":
    q1 = input("You come to a river, and you can walk around it or swim accross (swim/walk)? ")
    
    if q1 == "swim":
        print("You swam accross and were eatan by an alligator.")

    elif q1 == "walk":
        q11 = input("you walked for miles, get tired and dehydrated, and faint, so you will rest or keep walking (rest/walking)? ")
        
        if q11 == "rest":
            q111 = input("You wake up to a wild animal approaching, you run or stay still (run/still)? ")
            
            if q111 == "run":
                q1111 = input("You escape and find a cabin, you enter or ignore (enter/ignore)?")
                
                if q1111 == "enter":
                    print("You enter and you find food and shelter, and you WIN!")

                elif q1111 == "ignore":
                    print("You ignore it, and you get caught in a storm and freeze, and you lose!")

                else:
                    print("Not a valid option. You lose")

            elif q111 == "still":
                print("You still and the animal thinks you're dead and leaves. You WIN!!")
            
            else:
                print("Not a valid option. You lose.")

        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    q2 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross//back)?")
    
    if q2 == "back":
        print("You return home safely, but adventure ends.")

    elif q2 == "cross":
        q3 = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?")
        
        if q3 == "yes":
            q33 = input("You talk to the stranger and gives you a map to a hidden cave, you follow the map or burn it (follow/burn)? ")
            if q33 == "follow":
                print("The map leads to a cave with treasure. And you WIN")
            
            elif q33 == "burn":
                print("The map was cursed, you burn with it. And you lose.")

            else:
                print("Not a valid option. You lose.")

        elif q3 == "no":
            print("The stranger curses you. You get lost forever. And you lose.")

        else:
            print("Not a valid option. You lose.")
    
    else:
        print("Not a valid option. You lose.")

else: 
    print("Not a valid option. You lose.")

print(f"\nThank you for trying the game {name}! Every choice is a new story.")