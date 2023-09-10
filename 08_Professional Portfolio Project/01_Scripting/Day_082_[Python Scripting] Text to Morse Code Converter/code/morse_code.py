class MorseCode:
    INTERNATIONAL_MORSE_CODE = {
        'A': ".-",
        'B': "-...",
        'C': "-.-.",
        'D': "-..",
        'E': ".",
        'F': "..-.",
        'G': "--.",
        'H': "....",
        'I': "..",
        'J': ".---",
        'K': '-.-',
        'L': ".-..",
        'M': "--",
        'N': "-.",
        'O': "---",
        'P': ".--.",
        'Q': "--.-",
        'R': ".-.",
        'S': "...",
        'T': "-",
        'U': "..-",
        'V': "...-",
        'W': ".--",
        'X': "-..-",
        'Y': "-.--",
        'Z': "--..",

        '1': ".----",
        '2': "..---",
        '3': "...--",
        '4': "....-",
        '5': ".....",
        '6': "-....",
        '7': "--...",
        '8': "---..",
        '9': "----.",
        '0': "-----",

        ' ': "/",
    }

    horizontal_line = "----------------------------------------------------"

    hidden_code_to_end = "!OFF"
    hidden_code_to_show_the_code = "!CODE"

    def __init__(self):
        pass

    def intro_message(self):
        print(self.horizontal_line)
        print("Welcome to 'Morse Code Translater'!\n")

        print("*** Description **********************************")
        print("It can 'encode' letters into Morse Code, \n"
              "or 'decode' Morse Code into the original letters.\n")

        print("*** Example **************************************")
        print("1. Encoding\n"
              "[Input] HELLO\n"
              "[Output] .... . .-.. .-.. ---\n")

        print("2. Decoding\n"
              "[Input] .... . .-.. .-.. ---\n"
              "[Output] HELLO\n")

        print("*** Hidden Code **********************************")
        print(f"{self.hidden_code_to_end}: To turn off the program.")
        print(f"{self.hidden_code_to_show_the_code}: To see the list of Morse Code.")
        print("**************************************************")

        print("\nHave fun!")
        print(self.horizontal_line)

    def print_morse_code(self):
        print("\n*** International Morse Code ***")
        for key, value in self.INTERNATIONAL_MORSE_CODE.items():
            if key == '1':
                print(f"\n{key}: {value}")
            elif key == ' ':
                print(f"\n'{key}': {value}")
            else:
                print(f"{key}: {value}")

    def encode(self, user_input):
        try:
            temp = [self.INTERNATIONAL_MORSE_CODE[letter] for letter in user_input]
        except KeyError:
            # Special letter? Try to decode instead.
            return self.decode(user_input)
        else:
            output = ' '.join(temp)
            return output

    def decode(self, user_input):
        encoded_letters = user_input.split()
        key_list = list(self.INTERNATIONAL_MORSE_CODE.keys())
        values_list = list(self.INTERNATIONAL_MORSE_CODE.values())

        try:
            temp = [key_list[values_list.index(code)] for code in encoded_letters]
        except ValueError:
            # invalid input? Show the invalid letters.
            error_letters = []
            for string in encoded_letters:
                for letter in string:
                    if letter not in key_list:
                        error_letters.append(letter)

            error_message = "*** Error *****************************************************************\n" \
                            f"[Invalid input]:\n{','.join(error_letters)}\n" \
                            f"\n* General Note *\n"\
                            "-(X) It can not contain any special letters. (e.g. !@#$%^&*()[].,)\n"\
                            "-(O) It can only contain plain letters, numbers and spaces. (e.g. abc 1234)\n"\
                            "***************************************************************************\n"
            return error_message
        else:
            output = ''.join(temp)
            return output

