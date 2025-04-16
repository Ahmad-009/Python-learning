#Dictionaries

# dictionary = {
#     "Hello": 1,
#     "Bye":2,
# }
# dictionary["Loop"] = 3  # define a new key and word
# print(dictionary["Bye"]) # if u make spelling mixtake gives an error...and also if u type a word that doesnt exist also an error
# #dictionary = {} # empyts the dictionary
# dictionary["Bye"] = 4 #redefines the key
# print(dictionary["Bye"])

# for thing in dictionary:    # only gives key
#     print(thing)

# for thing in dictionary: # gives u both key and value
#     print(thing)
#     print(dictionary[thing])
#Nested lists and dictionaries
# dic1 = {
#     "car":1,
#     "bus":2,
# }
# dic2 = {
#     1:{dictionary},
#     2:{dic1}
# }
# print(dic2[1["Hello"]])

#Nested list inside a dictionary...remember that one key can only have one value
# travel_log = {
#     "France": ["Paris","Lille","Dijon"],
#     "Germany": ["Stuttgart,Berlin"]
# }
#print(travel_log["France"][1]) # to print lille

#Nested list example below
# nested_list = ['A','B',['C','D']]
# print(nested_list[2][1])

# #Dictionary within a dictionary
# travel_log = {
#     "France": ["Paris","Lille","Dijon"],
#     "Germany": {
#         "num_of_times_visited":8,
#         "cities_visited": ["Berlin","Hamburg","Stuttgart"]
#     },
# }
# print(travel_log["Germany"]["cities_visited"][2])

#Blind auction program below

print("""             ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\ """)
print("Welcome to the secret auction program \n")

bids = {}
condition = False
while not condition == True:
    name_of_the_bidder = input("What is your name? \n")
    bid = int(input("What's your bid? \n"))
    bids[name_of_the_bidder] = bid
    other_bidders = input("Are there any other bidders? Type yes or no \n")
    if other_bidders == "yes":
        print ("\n" * 100)
    elif other_bidders == "no":
        condition = True

best_bid = max(bids)
print(f"The best bid was made by {best_bid} which was {bids[best_bid]}")