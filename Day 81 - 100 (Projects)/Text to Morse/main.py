from art import logo

morse_dict = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",

}


def converter(text):
    user_morse = ""

    for char in text:
        if char in morse_dict:
            user_morse += morse_dict[char] + " "
        if char == " ":
            user_morse += "/"
    print(f"Your text in morse is: {user_morse}")


def start():
    print("Welcome to the Text to Morse Converter!")
    user_text = input("What Text would you like to convert to Morse?\n").upper()
    converter(user_text)


print(logo)
start()

user_choice = input("Do you have any more text to translate? Type 'Y' to continue, Type 'N' to Stop.").upper()
if user_choice == "Y":
    start()
else:
    print("Thank you for using this converter!")
