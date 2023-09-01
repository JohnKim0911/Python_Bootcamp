from tkinter import *
import random
import math


# text style
FONT_NAME = "Arial"
RED = "#ff0000"
BLUE = "#0000ff"
BLACK = "#000000"

# time
seconds = 15  # Change this if you want to change timer
timer_string = ""  # for displaying timer when it starts.
timer = None
is_first_turn = True
game_over = False

# word
word_list = ['mother', 'on', 'together', 'dad', 'look', 'by', 'family', 'fighting', 'try', 'me', 'top', 'upcoming',
             'new', 'my', 'texts', 'my', 'favorites', 'create', 'text', 'improve', 'your', 'typing', 'America', 'Speed',
             'Language', 'English', 'become', 'forum', 'feedback', 'contact', 'supporter', 'FAQ', 'open', 'chat',
             'typing', 'test', 'top', '200', 'words', 'typing', 'test', 'advanced', 'top', '1000', 'words', 'custom',
             'typing', 'test', 'create', 'your', 'own', 'multiplayer', 'typing', 'test', 'play', 'against', 'others']
word = random.choice(word_list)
word_count = 0


def enter(*event):
    global is_first_turn
    if is_first_turn:
        # For the first turn.
        # show word
        word_label.config(text=word)
        # turn on timer
        count_down(seconds)

        # For restart.
        # Clear warning message
        warning_label.config(text="")
        # change button to "Enter"
        enter_button.config(text="Enter")
        # un-highlight timer
        time_label.config(fg=BLACK)
        # set word count to 0 and un-highlight it
        global word_count
        word_count = 0
        word_count_label.config(text=word_count, fg=BLACK)

        is_first_turn = False
    else:
        next_word()


def sec_to_string_format():
    global seconds
    minute = math.floor(seconds / 60)
    sec = seconds % 60

    if sec < 10:
        sec = f"0{sec}"

    global timer_string
    timer_string = f"{minute}:{sec}"


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
        # highlight timer
        time_label.config(text=f"{count_min}:{count_sec}", fg=RED)

    if count > 0:
        time_label.config(text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # when time's up.
        # time's up message
        warning_label.config(text="Time's up!", font=(FONT_NAME, 13), fg=RED)
        # highlight word count
        word_count_label.config(text=word_count, fg=BLUE)
        # empty word
        word_label.config(text="")
        # empty input
        user_input.delete(0, END)
        # change button to "Restart"
        enter_button.config(text="Restart")

        global is_first_turn
        is_first_turn = True


def next_word():
    global word
    global word_count
    if user_input.get() == word:
        # when it is right answer
        # get new word
        new_word = random.choice(word_list)
        word_label.config(text=new_word)
        word = new_word
        # add count
        word_count += 1
        word_count_label.config(text=word_count)
        user_input.delete(0, END)
    else:
        warning_label.config(text="Wrong Answer.", font=(FONT_NAME, 11), fg=RED)


# ---------------------------- GUI ------------------------------- #
window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=20)
window.bind('<Return>', enter)

# row 0: title
title_label = Label(text="Typing Speed Test", font=(FONT_NAME, 15))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# row 1-0: "Time:"
time_indication_label = Label(text="Time:")
time_indication_label.grid(row=1, column=0, sticky='e')
# row 1-1: time
sec_to_string_format()
time_label = Label(text=timer_string)
time_label.grid(row=1, column=1, sticky='w')

# row 2-0: Count indication
word_count_indication_label = Label(text=f"Count:")
word_count_indication_label.grid(row=2, column=0, sticky='e')
# row 2-1: word_count
word_count_label = Label(text=word_count)
word_count_label.grid(row=2, column=1, sticky='w')

# row 3: word indication
word_indication_label = Label(text="Word:")
word_indication_label.grid(row=3, column=0, sticky='w')
# row 4: word
word_label = Label(text="", font=(FONT_NAME, 15, "bold"))
word_label.grid(row=4, column=0, columnspan=2, pady=5)

# row 5-0: input
user_input = Entry(width=20)
user_input.focus()
user_input.grid(row=5, column=0)
# row 5-1: Enter button
enter_button = Button(text="Enter", command=enter)
enter_button.grid(row=5, column=1)

# row 6-1: warning
warning_label = Label(text="Press 'Enter' to start.", fg=RED)
warning_label.grid(row=6, column=0, columnspan=2)


window.mainloop()


# For me...

# Align text with tkinter-grid
# i.e. grid(row=0, column=1, sticky='w')

# sticky = ‘e’ : Align to Right
# sticky = ‘w’: Align to Left
# sticky = ‘n’: Align to Top
# sticky = ‘s’: Align to bottom