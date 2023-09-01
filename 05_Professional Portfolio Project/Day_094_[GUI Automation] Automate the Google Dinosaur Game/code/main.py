# Install the required libraries
# pip install numpy
# pip install opencv-python
# pip install pyautogui

import cv2  # pip install opencv-python
import numpy as np
import pyautogui  # pip install PyAutoGUI

# Open your web browser and navigate to the following game:
# https://elgoog.im/dinosaur-game/

# Adjust the values below to define the region where obstacles appear in front of the dinosaur.
LEFT = 300  # Left coordinate of the region
TOP = 620  # Top coordinate of the region
WIDTH = 250  # Width of the region
HEIGHT = 250  # Height of the region

while True:
    # Capture a screenshot of the specified region to identify objects.
    # (Adjust the region location based on your screen.)
    image = pyautogui.screenshot(region=(LEFT, TOP, WIDTH, HEIGHT))  # left, top, width, and height

    # Convert the screenshot to a numpy array for use with OpenCV and convert its color format.
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Count the number of black and white pixels in the screenshot.
    # Pixels with values less than 100 are considered black, and those greater than 100 are considered white.
    black_pixel_count = np.sum(image < 100)
    white_pixel_count = np.sum(image > 100)

    # Print the pixel values for reference.
    print('Number of black pixels: ', black_pixel_count)
    print('Number of white pixels: ', white_pixel_count)

    # Check the pixel values to determine the mode (light or dark).
    # For light mode:
    if 4000 < black_pixel_count < 34000:  # Adjust the number of pixels if you need
        pyautogui.press('up')  # Press the 'up' button using pyautogui

    # For dark mode:
    if 4000 < white_pixel_count < 34000:
        pyautogui.press('up')

    # Display the captured image.
    cv2.imshow('image', image)

    # Check for the 'q' key press to exit the loop and close the window.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


# Thanks to this tutorial:
# https://youtu.be/UBLLtJG3lLw
# I just followed the instruction and then tried to understand.
