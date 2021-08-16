
# caesar cipher

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
            # 5 * -1 = -5
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
        # if the character inputed is not alphabet list(special characters) or numbers
        # then add to end_text e.g end_text = '_ _ _ _ _ 123'       
    print(f"The {cipher_direction}d text is {end_text}")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the encoded text is {cipher_text}")
        

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"the decrypted text is {plain_text}")
        
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# if direction == 'encode':
#     encrypt(plain_text = text, shift_amount = shift)
# if direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)


# how to ask the user if they want to restart the caesar program?
# e.g. type 'yes' if you want to go again. Otherwise type 'no'.
# if they type 'yes' then ask them for direction/text/shift again and called
# the caesar() function again

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # what if the user enters a shift that is greater than the number of letters in the alphabet?
    # in this case we use the modulo operator to get a smaller number that fits in the range
    # between 0 to 25
    shift = shift % 25
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print('Goodbye')

