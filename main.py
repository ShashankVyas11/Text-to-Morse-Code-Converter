morse_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}
header = """

 _______  _____   ______ _______ _____ _______ __   __
 |  |  | |     | |_____/ |______   |   |______   \_/  
 |  |  | |_____| |    \_ ______| __|__ |          |   


"""
running = True


def to_morse(text):
    """
    Translates from regular text to morse code. Unsupported characters will be ignored.
    :param str text: A string of text to translate. It may contain alphanumeric characters and some special characters,
    i.e. .,?!-/@().
    :return: Converted text into morse code. Individual characters are delimited by " " and words by "/".
    """
    morse = " ".join([morse_dict[char] for char in text.lower() if char in morse_dict.keys()])
    return morse


def to_text(morse):
    """
    Translates from morse code to regular text. Unsupported characters will be ignored.
    :param str morse: A string containing morse code using dots and dashes. Individual characters are delimited by " "
    and words by "/".
    :return: Translated morse code, all lowercase.
    """
    morse = "".join([char for char in morse if char in ".-/ "])
    text = "".join([list(morse_dict.keys())[list(morse_dict.values()).index(n)] for n in morse.split()])
    return text


while running:
    print(header)
    print("Welcome to the morse code translator! Choose an option to begin.")
    choice = input("1. Text --> Morse\n2. Morse --> Text\n3. Exit\n")
    if choice == "1":
        output = to_morse(input("Type in the text you want to convert to morse code. Untranslatable characters will "
                                "be ignored.\nInput: "))
        print(f"Output: {output}")
    elif choice == "2":
        output = to_text(input("Type in the morse code you would like to decipher. Individual characters must be "
                               "delimited by ' ' and words by '/', any other characters will be ignored.\nInput: "))
        print(f"Output: {output}")
    elif choice == "3":
        running = False
    print("\n\n\n")