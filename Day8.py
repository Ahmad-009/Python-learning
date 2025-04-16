# def greet(name,location):
#     print(f"Hello my name is {name} and i live in {location}")
# greet(location = "bahawalpur", name = "ahmad")

# def calculate_love_score(name1 , name2):
#     letters = ['t','r','u','e','l','o','v','e']
#     total_name = name1+name2
#     count = 0
#     for letter in letters:
#         if letter in total_name:
#             count += 1
#         else:
#             pass
#     print(count)
# calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")
def caesar_cypher(direction,word,shift_number):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']
    if direction == 'encrypt':
             encrypted_word = ''
             for i in word:
                position = letters.index(i)
                new_postion = (position + shift_number) % 26
                i = letters[new_postion]
                encrypted_word += i
             print(encrypted_word)
    elif direction == 'decrypt':
           decrypted_word = ''
           for i in encrypted_word:
                position = letters.index(i)
                new_postion = (position - shift_number) % 26
                i = letters[new_postion]
                decrypted_word += i
           print(decrypted_word)
    else:
          print("Please enter the correct word")

direction = input("What do u want to do encrypt or decrypt or exit: \n")
word = input("Write the word u want to encrypt: \n")
shift_number = int(input("Tell the shift number \n"))
caesar_cypher(direction,word,shift_number)
