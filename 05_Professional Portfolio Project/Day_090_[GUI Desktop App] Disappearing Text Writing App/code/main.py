# [GUI Desktop App]_Disappearing Text Writing App
# it should allow a user to type and if they stop for more than 5 seconds,
# it should delete everything they've written so far.

from tkinter import *
import math


class Application(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self)
        self.pack()

        self._after_id = None  # for "handle_wait" function: Is the user typing?

        self.text = Text(self)
        self.text.pack()
        self.text.bind('<Key>', self.handle_wait)  # catch when user types something.

        # For count_down
        self.should_timer_on = False
        self.timer = None

    def handle_wait(self, event):
        # cancel the old job
        if self._after_id is not None:
            self.after_cancel(self._after_id)
            self.should_timer_on = False

        # create a new job
        # when user stops typing for 1 sec, start count-down.
        # 1000ms => 1seconds
        self._after_id = self.after(1000, self.start_count_down)  # Change the number here to test.

    def start_count_down(self):
        self.should_timer_on = True
        self.count_down(5)  # starting seconds of count_down

    def count_down(self, seconds):
        # format: seconds to minutes & seconds. (0:70 -> 1:10)
        count_min = math.floor(seconds / 60)
        count_sec = seconds % 60

        # format: when it's less than 10 sec left. (0:4 -> 0:04)
        if count_sec < 10:
            count_sec = f"0{count_sec}"
            time_label.config(text=f"{count_min}:{count_sec}", fg="red")
        # real count-down

        if self.should_timer_on:
            if seconds > 0:
                time_label.config(text=f"{count_min}:{count_sec}")
                self.timer = window.after(1000, self.count_down, seconds - 1)
            else:
                # When time is over
                time_label.config(text="0:00")
                self.text.delete('1.0', END)  # Clear Text
                self._after_id = None  # Reset
        else:
            # stop counting-down
            time_label.config(text="")
            return


# ---------------------------- GUI ------------------------------- #
window = Tk()
window.title("Disappearing Text Writing App")
window.config(padx=50, pady=20)

time_label = Label(text="", font=("Arial", 15, "bold"))
time_label.pack()

app = Application(window)
app.mainloop()