import random
# fruits = ["Apple", "Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
score = [1,3,2]
# total = sum(score)
# print(total)
# temp = 0
# for s in score:
#     if s > temp:
#         temp = s
#     else:
#         continue
# print(f"Max number is {temp}")
# range function
# total = 0
# for num in range(1,101):
#     total += num
# print(total)

# for num in range(1,101):
#     if num % 3 == 0:
#         print("Fizz\n")
#     elif num % 5 == 0:
#         print("Buzz\n")
#     elif num % 5 and num % 3:
#         print("FizzBuzz\n")
#     else:
#         continue

lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of uppercase alphabets
uppercase_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# List of common symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', ';', ':', '"', "'", ',', '.', '/', '<', '>', '?']

# List of numbers (as strings)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
final_list = numbers + symbols + lowercase_alphabets + uppercase_alphabets
print("Welcome to the PyPassword Generator! \n")
letter = int(input("How many letters would u like in ur password\n"))
symbol = int(input("How many symbols would u like in ur password\n"))
number = int(input("How many numbers would u like in ur password\n"))
total_length = letter + symbol + number
final_password = ""
random_password = ""
temp = ""
for password in range(1,letter+1):
     final_password += random.choice(lowercase_alphabets)
for password in range(1,symbol+1):
     final_password += random.choice(symbols)
for password in range(1,number+1):
     final_password += random.choice(numbers)
print(f"Your generated password is: {final_password}")
print(random.choice(final_password))
for r in range(1,len(final_password)+1):
     temp = random.choice(final_password)
     final_password -= final_password
     random_password += temp