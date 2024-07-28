from tkinter import *
import pandas as pd
import time
import random
flash=""
AG=True
FONT_NAME = "Courier"

a=pd.read_csv(r"R:\100 day of code\31th\data\french_words.csv")
dict_word={}
for _,value in enumerate(a["French"]):
    dict_word[value]=a["English"][_]
word_list=[a for a in dict_word]
print(word_list)





BACKGROUND_COLOR = "#B1DDC6"
def flash_card():
    global card_front

    global flash
    try:
        flash = random.choice(word_list)
    except IndexError or ValueError:
        card_front.delete('all')
        card_front.create_text(410, 200, text="Congratulations you learned \nall the words ", font=(FONT_NAME, 25, "bold"))
        win.update()
    else:
        print(flash)


        card_front.create_image(410, 269, image=card_front_photu)
        card_front.create_text(410, 200, text=front_text, font=(FONT_NAME, 25, "bold"))
        card_front.create_text(410, 269, text=f"{flash}", font=(FONT_NAME, 35, "bold"))
        card_front.grid(column=0, row=0, columnspan=2)

        wrong_button=Button(image=wrong_pic,command=answer_wrong)
        wrong_button.grid(column=0, row=1, sticky=W, padx=100)
        # wrong = Canvas(width=98, height=98)
        # wrong.create_image(50, 50, image=wrong_pic, tag="wrongpic")
        # wrong.tag_bind("wrongpic", '<ButtonPress-1>', answer_wrong)
        # wrong.grid(column=0, row=1, sticky=W, padx=100)

        # right = Canvas(width=98, height=98)
        # right.create_image(50, 50, image=right_pic, tag="rightpic")
        # right.tag_bind("rightpic", '<ButtonPress-1>', answer_right)
        # right.grid(column=1, row=1, sticky=E, padx=100)
        right_button = Button(image=right_pic, command=answer_right)
        right_button.grid(column=1, row=1, sticky=E, padx=100)

        win.after(3000,func=flip)


        win.update()
def answer_right():
    # print(f"answer is right {_}")
    global flash
    global card_front
    try:
        word_list.remove(flash)
        flash_card()
    except IndexError and ValueError:
        card_front.create_text(410, 200, text="Congratulations you learned all the words", font=(FONT_NAME, 25, "bold"))
        win.update()

def flip():
    card_front.create_image(410, 269, image=card_back_photu)
    card_front.create_text(410, 200, text=back_text, font=(FONT_NAME, 25, "bold"))
    card_front.create_text(410, 269, text=f"{dict_word[flash]}", font=(FONT_NAME, 35, "bold"))
def answer_wrong():
    print(f"answer is wrong")
    flash_card()


win=Tk()
win.config(bg=BACKGROUND_COLOR,width=1200,height=926,pady=50,padx=50)
win.title("Learn French")

card_front_photu = PhotoImage(file="./images/card_front.png")
wrong_pic=PhotoImage(file="./images/wrong.png")
right_pic=PhotoImage(file="./images/right.png")
card_back_photu=PhotoImage(file="./images/card_back.png")
front_text = "French"
back_text = f"English"
card_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card()







win.mainloop()









win.mainloop()

