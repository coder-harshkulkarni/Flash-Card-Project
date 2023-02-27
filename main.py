from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/hindi_words.csv")
to_learn = data.to_dict(orient="records")


def change_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(word, text=random_word["English"], fill="black")
    canvas.itemconfig(title, text="English", fill="black")
    canvas.itemconfig(card, image=fg_img)
    flip_timer = window.after(3000, func=change_bg)


def change_word_remove():
    to_learn.remove(random_word)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    change_word()


def change_bg():
    canvas.itemconfig(card, image=bg_img)
    canvas.itemconfig(title, text="Hindi", fill="white")
    canvas.itemconfig(word, fill="white", text=random_word["Hindi"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=change_bg)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
fg_img = PhotoImage(file="images/card_front.png")
bg_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=fg_img)
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=change_word_remove)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_button.grid(column=0, row=1)

change_word()
window.mainloop()
