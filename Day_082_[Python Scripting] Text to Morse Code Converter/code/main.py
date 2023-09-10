from morse_code import MorseCode

morse = MorseCode()
morse.intro_message()

is_on = True
while is_on:
    user_input = input("[Input]:\n").upper()

    if user_input == "!CODE":
        morse.print_morse_code()
    elif user_input == "!OFF":
        print("*** The program is turned off. ***")
        is_on = False
    else:
        output = morse.encode(user_input)
        print(f"\n[Output]:\n{output}\n")

    print(morse.horizontal_line)

