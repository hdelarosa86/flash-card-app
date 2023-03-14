from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

#DATA

try:
    with open('./data/words_to_learn.csv', 'r') as data_file:
        data = pandas.read_csv(data_file)
except FileNotFoundError:
    data_df = pandas.read_csv('./data/french_words.csv')
    words_to_learn = data_df.to_dict(orient='records')
else:
    words_to_learn = data.to_dict(orient='records')


# FUNCTIONS


def flip_card():
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=current_word['English'], fill='white')
    canvas.itemconfig(canvas_image, image=card_back)


def get_new_word():
    global current_word, flip_timer

    window.after_cancel(flip_timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word, text=current_word['French'], fill='black')
    canvas.itemconfig(language, text='French', fill='black')
    flip_timer = window.after(3000, flip_card)


def is_known():
    words_to_learn.remove(current_word)
    new_data_df = pandas.DataFrame(words_to_learn)
    new_data_df.to_csv('./data/words_to_learn.csv', index=False)
    get_new_word()


# WINDOW
window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

# IMAGES
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')


# CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
right_button = Button(image=right_img, borderwidth=0, command=is_known)
right_button.grid(column=1, row=1, padx=50)
wrong_button = Button(image=wrong_img, borderwidth=0, command=get_new_word)
wrong_button.grid(column=0, row=1, padx=50)

get_new_word()
window.mainloop()
