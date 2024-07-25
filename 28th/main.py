from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check="✔"
reps=1
clock=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_all():
    global clock
    global reps
    reps=1
    timer_label.config(text="Start",font=(FONT_NAME,35,"bold"),fg=GREEN)
    canvus.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    win.after_cancel(clock)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clock():
    global check
    global reps
    sec=60
    if reps%2==1:
        countdown(sec*WORK_MIN)
        timer_label.config(text="Work",fg=GREEN)
        reps+=1
    elif reps%2==0 and reps%8!=0:
        countdown(sec * SHORT_BREAK_MIN)
        check_label.config(text=check * math.floor(reps / 2))
        timer_label.config(text="Rest",fg=PINK)
        reps+=1

    elif reps%8==0:
        countdown(sec*LONG_BREAK_MIN)
        check_label.config(text=check * math.floor(reps / 2))
        timer_label.config(text="Rest",fg=RED)
        reps+=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    global clock
    minutes=math.floor(time/60)
    seconds=time%60
    if seconds==0:
        seconds="00"
    elif seconds<10:
        seconds=f"0{seconds}"
    canvus.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time>0:
        clock=win.after(1000,countdown,time-1)
    if time==0:
        start_clock()


# ---------------------------- UI SETUP ------------------------------- #
win=Tk()
win.title("Pomodoro")
win.config(padx=100,pady=50,bg=YELLOW)

timer_label=Label(text="Start",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

check_label=Label(font=(FONT_NAME,10,"bold"),fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=3)

canvus=Canvas(height=224,width=200,bg=YELLOW,highlightthickness=0)
photu=PhotoImage(file="tomato.png")
canvus.create_image(100,112,image=photu)
timer_text=canvus.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvus.grid(column=1,row=1)


start=Button(text="Start",font=(FONT_NAME,8,"bold"),command=start_clock)
start.grid(column=0,row=2)

reset=Button(text="Reset",font=(FONT_NAME,8,"bold"),command=reset_all)
reset.grid(column=2,row=2)










win.mainloop()