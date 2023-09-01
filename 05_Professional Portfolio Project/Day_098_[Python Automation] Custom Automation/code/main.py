# You should change the positions on the code before running the program,
# since it cannot automatically detect where the buttons are.

import os
import time
import pyautogui


folder_path = 'C:\\Users\\User\\Desktop\\Things to print out'
files = os.listdir(folder_path)
# print(files)

for file in files:
    os.startfile(f"{folder_path}\\{file}")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'p')  # Open "Print page"
    time.sleep(3)
    # print(pyautogui.position())
    pyautogui.click(x=459, y=744)  # Click "Fill page" to switch to "Shink to fill"
    # print(pyautogui.position())
    pyautogui.click(x=None, y=779)  # Click "Shink to fill"
    pyautogui.press('tab', presses=2)  # Move to "Print" Button
    time.sleep(1)
    pyautogui.press('enter')  # Print
    time.sleep(1)
    new_file_name = f"{file[:-4]}.pdf"
    # print(new_file_name)
    pyautogui.write(new_file_name)  # Write PDF file name
    time.sleep(1)
    pyautogui.press('enter')  # Save PDF file
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')  # Close "Print page"
    print(f"{new_file_name}: Done")
    time.sleep(1)

print("All Done!")




