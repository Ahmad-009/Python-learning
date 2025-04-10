import random
#import module_testing
# print(module_testing.num)

# num = random.random() * 10 # number is between 0 and 1 ...not including 1
# fnum = random.uniform(4,7) # generates float number between these
# print(num)
# print(fnum)

# number = random.random()
# if number >= 0.5:
#     print("Heads!!!")
# else:
#     print("Tails!!!")

# states = ["punjab","sindh","kpk","balochistan"]
# states[1] = "Sindh"
# states.append("Gilgit") # use python documentation for more functions of list
# print(states)

# friends = ["Alice","Bob","Charlie","David","Emanuel"]
# random_number = random.randint(0,4)
# print(f"{friends[random_number]} will pay the bill...Hooray!!!")

# #another approach is this..to find a random function
# print(print(f"{random.choice(friends)} will pay the bill...Hooray!!!"))

#nested lists...list within a list
# dirty_dozen_produce = [
#     "Strawberries",           # Fruit
#     "Spinach",                # Vegetable
#     "Kale, Collard & Mustard Greens",  # Vegetables
#     "Grapes",                 # Fruit
#     "Peaches",                # Fruit
#     "Pears",                  # Fruit
#     "Nectarines",             # Fruit
#     "Apples",                 # Fruit
#     "Bell Peppers & Hot Peppers",  # Vegetables
#     "Cherries",               # Fruit
#     "Blueberries",            # Fruit
#     "Green Beans"             # Vegetable
# ]
# # Fruits from the Dirty Dozen 2024
# dirty_dozen_fruits = [
#     "Strawberries",
#     "Grapes",
#     "Peaches",
#     "Pears",
#     "Nectarines",
#     "Apples",
#     "Cherries",
#     "Blueberries"
# ]

# # Vegetables from the Dirty Dozen 2024
# dirty_dozen_vegetables = [
#     "Spinach",
#     "Kale, Collard & Mustard Greens",
#     "Bell Peppers & Hot Peppers",
#     "Green Beans"
# ]
# dirty_dozen_produce = [dirty_dozen_fruits,dirty_dozen_vegetables]
# print([dirty_dozen_produce[1][1]])

rock = '''
                                             
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
'''
paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        
''' 

scissors = '''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''
user_player = int(input("what do you choose? Type 0 for rock,1 for paper or 2 for scissors: \n"))
comp_player = random.randint(0,2)

if user_player == comp_player:
    print("Same move try again!!!\n")
elif user_player == 0 and comp_player == 1:
    print("U chose " + rock + "\n")
    print("Comp chose " + paper + "\n")
    print("That means u lose!!!\n")
elif user_player == 1 and comp_player == 0:
    print("U chose " + paper + "\n")
    print("Comp chose " + rock + "\n")
    print("That means u win!!!\n")
elif user_player == 0 and comp_player == 2:
    print("U chose " + rock + "\n")
    print("Comp chose " + scissors + "\n")
    print("That means u win!!!\n")
elif user_player == 2 and comp_player == 0:
    print("U chose " + scissors + "\n")
    print("Comp chose " + rock + "\n")
    print("That means u lose!!!\n")
elif user_player == 1 and comp_player == 2:
    print("U chose " + paper + "\n")
    print("Comp chose " + scissors + "\n")
    print("That means u lose!!!\n")
elif user_player == 2 and comp_player == 1:
    print("U chose " + scissors + "\n")
    print("Comp chose " + paper + "\n")
    print("That means u win!!!\n")
else:
    print("Police is here ...u played a forbidden move...run away as fast as u can!!!")