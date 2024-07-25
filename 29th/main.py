from tkinter import *
import random
from tkinter import messagebox
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
pass_len=random.randint(8,10)
symbols_count=random.randint(2,4)
numeric_count=random.randint(2,4)
def passgen():
    alphabets=[random.choice(letters) for _ in range(pass_len)]
    numeric=[random.choice(numbers) for _ in range(numeric_count)]
    symbolls=[random.choice(symbols) for _ in range(symbols_count)]

    pass_li=alphabets+numeric+symbolls
    random.shuffle(pass_li)
    new_pass="".join(pass_li)
    return new_pass
def out_pass():
    password_input.delete(0,END)
    a=passgen()
    pyperclip.copy(a)
    password_input.insert(0,a)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def sav_pass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if ((len(website)==0 or len(password)==0 or len(email)==0 )):
        bad_entry=messagebox.showwarning(title="Bad Entry",message="Looks like you left one of the fields empty")
    else :
        confirm=confirm_save=messagebox.askokcancel(title=website,message=f"These are the values entered :\nEmail : {email} \nPassword : {password} \nDo you want to save the details provided ?")

        if confirm:
            with open("data.txt",'a') as file:
                website_input.delete(0, END)
                password_input.delete(0, END)
                file.write(f"{website} , {email}  , {password}\n")
# ---------------------------- UI SETUP ------------------------------- #

win=Tk()
win.title("Password Generator")
win.config(padx=50,pady=50)

canvus=Canvas(width=200,height=200)
lock=PhotoImage(file="logo.png")
canvus.create_image(100,100,image=lock)
canvus.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)






website_input=Entry(win,width=35)
website_input.grid(column=1,row=1,columnspan = 2,sticky=E+W)
website_input.focus()


email_input=Entry(win,width=35)
email_input.grid(column=1,row=2,columnspan = 2,sticky=E+W)
email_input.insert(0,"xyzzz4@gmail.com")

password_input=Entry(win,width=21)
password_input.grid(column=1,row=3,sticky=E+W)

gen_pass=Button(text="Generate Password",command=out_pass)
gen_pass.grid(column=2,row=3,sticky=E+W)


add=Button(text="Add",width=36,command=sav_pass)
add.grid(column=1,row=4,columnspan=2,sticky=E+W)



win.mainloop()