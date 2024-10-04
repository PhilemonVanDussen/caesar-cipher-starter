alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message = ""

user_message = input("Enter your secret message: ")
# print(user_message)
key = int(input("Enter a key: "))

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_message + new_character

print("Your new message is " + new_message)