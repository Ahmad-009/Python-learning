#if else
#conditional operators
# >= <= == > < != 
# modulu operator % gives remainder

# use of module and if and else uses
# number = int(input("Input a number \n"))
# if number % 2 == 0:
#     print(f"The number {number} is even! \n")
# else:
#     print(f"The number {number} is odd! \n")

# print("Welcome to Python Pizza Deliveries! \n")
# size = input("What size pizza do you want? S, M or L: \n")
# bill = 0

# if size == "S":
#     bill = 15
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
#     extra_cheese = input("Do you want extra cheese? Y or N: \n")
#     if pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "M":
#     bill = 20
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
#     extra_cheese = input("Do you want extra cheese? Y or N: \n")
#     if pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "L":
#     bill = 25
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
#     extra_cheese = input("Do you want extra cheese? Y or N: \n")
#     if pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# else:
#     print("Please enter correct input \n")
# print(f"Your final bill is ${bill}")

# logical operatos ...multiple condition check
# or and not

print('''

     _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
      '''
)
print("Welcome to Treasure Island \n")
print("Your mission is to find the treasure \n")

action = input("You're at a crossroad. Where do you want to go?\n Left or right?\n")
if action == "Right" or action == "right":
    print("Fall into a hole....GAME OVER!")
elif action == "Left" or action == "left":
    print("U were saved by God's grace...u moved left")
    action = input("Swim or wait here?")
    if action == "Swim" or action == "swim":
        print("Attacked by an anaconda...patience is key...GAME OVER!")
    elif action == "Wait" or action == "wait":
        print("U were saved by a Gandalf...Hurrah!!!")
        action = input("Which door? Red...Blue..or Yellow?")
        if action == "Red" or action == "red":
            print("Burned by the devil himself...GAME OVER!")
        elif action == "Blue" or action == "blue":
            print("Eaten by the Seath the Scaleless...GAME OVER!")
        elif action == "Yellow" or action == "yellow":
            print("WOW...Rare W...U win!!!...Here's ur treasure of $5 million dollars!!!")
        else:
            print("Ahh!!...Wrong input...U were so close u Donut!!!")
    else:
        print("U entered the wrong command u doofus!..GAME OVER")
else:
    print("U entered the wrong command....Game over")
# use .lower() function to lower the input by the user