# # import tkinter as tk
# #
# #
# # def button_press():
# #     global a
# #     buton1["text"]="Submitted"
# #     labul.config(text=inpuut.get())
# # window=tk.Tk()
# # window.title("APP")
# # window.minsize(width=800,height=600)
# #
# #
# #
# # labul=tk.Label(text="Hi how are u ",font=("Arial",24,"bold"))
# # labul.pack()
# #
# #
# #
# # buton1=tk.Button(text="Submit",font=("Arial",24,"bold"),command=button_press)
# # buton1.pack()
# #
# # inpuut=tk.Entry(width=30)
# # inpuut.pack()
# #
# #
# #
# #
# #
# #
# #
# #
# # window.mainloop()
#
#
#
#
#
#
# from tkinter import *
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
#
#
#

import tkinter as tk

x="0"
def calcul():
    text3.config(text=str((float(input.get()))*1.609))



win=tk.Tk()
# win.minsize(width=200,height=150)
win.config(padx=10,pady=10)


input=tk.Entry(width=10)
input.grid(column=1,row=0)


text=tk.Label(text="Miles")
text.grid(column=2,row=0)

text2=tk.Label(text="is equal to ")
text2.grid(column=0,row=1)

text3=tk.Label(text=x)
text3.grid(column=1,row=1)

text4=tk.Label(text="Km")
text4.grid(column=2,row=1)


buton=tk.Button(width=10,text="Calculate",command=calcul)
buton.grid(column=1,row=2)













win.mainloop()























