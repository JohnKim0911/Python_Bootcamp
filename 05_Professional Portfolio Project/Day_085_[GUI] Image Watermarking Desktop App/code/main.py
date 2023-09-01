from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont


GUI_LABEL_FONT = 'Aerial 15 bold'
image_path = ""
watermark = ""


def select_file():
    global image_path
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[
        ("image", ".jpg"),
        ("image", ".jpeg"),
        ("image", ".png"),
        ('all files', '.*'),
    ])
    # display path
    Label(window, text=image_path, font=13).grid(row=1, column=0, columnspan=2)


def get_watermark():
    global watermark
    watermark = watermark_input.get()
    # display watermark
    Label(window, text=watermark, font=13).grid(row=3, column=0, columnspan=2)


def save():
    # calculate where to put watermark
    image = Image.open(image_path)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 36)
    text_width, text_height = draw.textsize(watermark, font)
    margin = 20
    x = width - text_width - margin
    y = height - text_height - margin

    # add watermark
    draw.text((x, y), watermark, font=font)

    # save as
    filetypes = [("image", "*.jpg"),
                 ("image", "*.jpeg"),
                 ("image", "*.png"),
                 ('all files', '*.*')]
    file = filedialog.asksaveasfile(filetypes=filetypes, defaultextension=filetypes)
    image.save(file)

    # pop up message
    messagebox.showinfo('Information', 'Success!')


window = Tk()
window.title("Image Watermarking Desktop App")
window.config(padx=50, pady=20)

# 1. Select an image.
Label(window, text="1. Select an image.", font=GUI_LABEL_FONT).grid(row=0, column=0, padx=10, pady=20, sticky='e')
select_button = Button(window, text="Select an image", width=20, height=3, command=select_file)
select_button.grid(row=0, column=1, pady=20, sticky='w')
# display for Path
Label(window, text="").grid(row=1, column=0, columnspan=2)

# 2. Watermarking Text.
Label(window, text="2. Watermarking Text:", font=GUI_LABEL_FONT).grid(row=2, column=0, padx=10, pady=20, sticky='e')
watermark_input = Entry(width=24)
watermark_input.grid(row=2, column=1, pady=20, sticky='w')
enter_button = Button(window, text="Enter", command=get_watermark)
enter_button.grid(row=2, column=2, pady=20)
# space for Watermarking
Label(window, text="").grid(row=3, column=0, columnspan=2)

# 3. save.
Label(window, text="3. Select where to save.", font=GUI_LABEL_FONT).grid(row=4, column=0, padx=10, pady=20, sticky='e')
save_button = Button(window, text="Save", width=20, height=3, command=save)
save_button.grid(row=4, column=1, pady=20, sticky='w')

window.mainloop()
