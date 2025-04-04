# print('hello'[-1]) #subscripting
# print(123_456_789) #better help to visualize

# length = len(str(1235))   # to give length of something
# type_of = type("1235")    # to check type of something
# print(length)
# print(type_of)

# typecasting below

# print("Number of letters in ur name is: " + str(len(input("Enter ur name: "))))

# mathmetical operators

# print(5/3) # div (float)
# print(5//3) # div (int)
# print(2**3) # power

# pemdas rule Parenthesis,Exponents,mult,div,add,sub
# div and mult r same priority..but the left one gets executed first

# print(round(10.6)) # rounds in mathemetical sense....round(bmi,2) this rounds to 2
# assignemnt operators
#+= -= *= /=
#f-strings
# print(f"your score is: {30}")

print("Welcome to the tip calculator! \n")
total_bill = float(input("What was the total bill? \n"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? \n"))
num_of_people = int(input("How many people to split the bill? \n"))
final_bill = (total_bill*(12/100) + total_bill) / num_of_people
rounded_final_bill = round(final_bill,2)
print(f"each person should pay: ${rounded_final_bill}")
