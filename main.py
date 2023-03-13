from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
#DATA
french_words_df = pandas.read_csv('./data/french_words.csv')
french_words_list = french_words_df.to_dict(orient='records')


def get_word():
    random_word = random.choice(french_words_list)
    keys = list(random_word.keys())
    values = list(random_word.values())
    return keys, values


def new_word():
    words = get_word()
    canvas.itemconfig(word, text=words[1][0])

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
initial_word = get_word()
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text=initial_word[0][0], font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text=initial_word[1][0], font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)


right_button = Button(image=right_img, borderwidth=0, command=new_word)
right_button.grid(column=1, row=1, padx=50)
wrong_button = Button(image=wrong_img, borderwidth=0, command=new_word)
wrong_button.grid(column=0, row=1, padx=50)

window.mainloop()

