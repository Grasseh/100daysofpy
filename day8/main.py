import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text, shift, direction):
    final_text = ''
    for character in text:
        if character in alphabet:
            if direction == "encode":
                final_text += alphabet[(alphabet.index(character) + shift) % 26]
            else:
                final_text += alphabet[(alphabet.index(character) - shift) % 26]
        else:
            final_text += character
    print(f"The {direction}d text is {final_text}")

keep_going = True
while(keep_going):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    keep_going = input("Do you want to encode or decode again? Type 'yes' if you do, anything else if you want to stop. ") == 'yes'
