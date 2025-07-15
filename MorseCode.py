## converting string to morseCode in python --------------------
morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

input_message = (input("Enter Your Message: ").upper())

def convert_to_morse_code(input_message):
    translatedMessage = ""
    for char in input_message:
        if char in morseCode:
            translatedMessage+=morseCode[char]
            print(f"The letter {char} is converted to: {morseCode[char]}")
        else:
            translatedMessage +=" "
    # print(f"Your Message \"{input_message}\" is Converted to Morse Code: {translatedMessage}")
    # print(f"length of {input_message}",len(input_message))
    # print(f"length of {translatedMessage} is",len(translatedMessage))
    return translatedMessage

print("MorseCode:",convert_to_morse_code(input_message))
