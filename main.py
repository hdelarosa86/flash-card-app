from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# WINDOW
window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# IMAGES
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

# CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_img, borderwidth=0)
right_button.grid(column=1, row=1, padx=50)
wrong_button = Button(image=wrong_img, borderwidth=0)
wrong_button.grid(column=0, row=1, padx=50)

window.mainloop()

