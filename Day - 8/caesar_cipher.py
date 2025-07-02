# from art import Logo

# print(logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    
]


# def encrypt(text, shift):
#     calculated_text = ""

#     for letter in text:
#         shift_position = alphabet.index(letter) + shift
#         shift_position %= len(alphabet)
#         calculated_text +=alphabet[shift_position]

#     print(f"Here is the encode results: {calculated_text}")

# def decrypt(text, shift):
#     calculated_text = ""

#     for letter in text:
#         shift_position = alphabet.index(letter) - shift
#         shift_position %= len(alphabet)
#         calculated_text +=alphabet[shift_position]

#     print(f"Here is the encode results: {calculated_text}")

def ceasar(direction_given, texting, shifting):

    calculated_text = ""
    if direction_given=="decode":
        shifting *= -1

    for letter in texting:
        if letter not in alphabet:
            calculated_text +=letter
        else:
            shift_position = alphabet.index(letter) + shifting
            shift_position %= len(alphabet)
            calculated_text +=alphabet[shift_position]

    print(f"Here is the {direction_given}d results: {calculated_text}")


    # if direction_given == "encode":
    #     encrypt(text=text, shift=shift)
    # elif direction_given == "decode":
    #     decrypt(text = text, shift=shift)

try_again = True

while try_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message\n").lower()
        shift = int(input("Type your shift number\n"))
        # if shift not number:
        #     print("Enter number from 1-9")
        ceasar(direction_given=direction, texting=text, shifting=shift)
        restart = input("Type 'yes' if you want to do again. Otherwise, type 'no', \n")
        if restart == "no":
            try_again =False
            print("Goodbye")
    else:
        print("Invalid Input ! please enter correct keyword.")