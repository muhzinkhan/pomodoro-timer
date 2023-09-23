from tkinter import *
import tkinter.messagebox
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Segoe UI Semibold"
WORK_MIN = 25          # 25
SHORT_BREAK_MIN = 5     # 5
LONG_BREAK_MIN = 20     # 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro")
    check_marks.config(text="")
    global reps
    reps = 0
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    start_button.config(state="disabled")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 30))
        tkinter.messagebox.showinfo("Long Break", "Time to take a long break!")
        # lbreak_noti = Toplevel()
        # lbreak_noti.title('lbreak_noti')
        # Message(lbreak_noti, text="Time to take a long break!", padx=20, pady=20).pack()
        # lbreak_noti.after(5000, lbreak_noti.destroy)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Shot Break", fg=PINK, font=(FONT_NAME, 33))
        tkinter.messagebox.showinfo("Shot Break", "Time to take a short break!")
        # sbreak_noti = Toplevel()
        # sbreak_noti.title('sbreak_noti')
        # Message(sbreak_noti, text="Time to take a short break!", padx=20, pady=20).pack()
        # sbreak_noti.after(5000, sbreak_noti.destroy)
    else:
        count_down(work_sec)
        title_label.config(text="⏱️Work⏱️", fg=GREEN, font=(FONT_NAME, 37))
        if not reps == 1:
            tkinter.messagebox.showinfo("Work", "Time to work!")
            # work_noti = Toplevel()
            # work_noti.title('work_noti')
            # Message(work_noti, text="Time to work!", padx=20, pady=20).pack()
            # work_noti.after(5000, work_noti.destroy)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(989, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.iconbitmap("assets/pomodoro.ico")
window.minsize(width=590, height=440)

title_label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="assets/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, height=2, width=10)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, height=2, width=10)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
