from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, direction):
    end_text = ''
    if direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        #Check char is letter or not
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {direction} text is {end_text}')


print(logo)

yes_or_no = True
while yes_or_no:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: User enters a shift that is greater than the number of letters in the alphabet
    shift %= 26

    caesar(text, shift, direction)
    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        yes_or_no = False
        print('Good Bye')
