# pomodoro project
import sys
from tkinter import Button, Tk, Canvas, Label, PhotoImage
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK="#e2979c"
RED="#e7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"
FONT_NAME="Courier"
WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
repos=0
timer=0


def count_timer(count):
	count_min=math.floor(count / 60)
	count_sec=count % 60
	if count_sec < 10:
		count_sec=f"0{count_sec}"
	canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	
	if count > 0:
		global timer
		timer=window.after(1000, count_timer, count - 1)
	else:
		start_timer()
		marks=""
		work_sessions=math.floor(repos / 2)
		for _ in range(work_sessions):
			marks+="✔"
		check_marks.config(text=marks)


def start_timer():
	global repos
	repos+=1
	work_sec=WORK_MIN * 60 * 1
	short_break_sec=SHORT_BREAK_MIN * 60
	long_break_sec=LONG_BREAK_MIN * 60
	
	if repos % 8 == 0:
		count_timer(long_break_sec)
		title_label.config(text="Break", fg=RED)
		# title_label.grid(row=1, column=3)
	
	elif repos % 2 == 0:
		count_timer(short_break_sec)
		# timer_tick=canvas.create_text(280, 450, fill="green", font="Times 30 bold", text="✔")
		title_label.config(text="short break", fg=PINK)
		# title_label.grid(row=1, column=3)
	
	else:
		count_timer(work_sec)
		title_label.config(text="Work", fg=GREEN)
		# title_label.grid(row=1, column=3)


def reset_timer():
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text="00:00")
	title_label.config(text="Timer")
	check_marks.config(text="")
	
	global repos
	repos=0


window=Tk()
window.title("pomodoro")
window.config(padx=280, pady=10, bg="yellow")
title_label=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=3, row=1)

tomato_image=PhotoImage(file="tomato.png")
canvas=Canvas(window, height=600, width=600, bg="yellow", highlightthickness=0)
canvas.grid(row=2, column=3)
canvas.create_image(300, 300, image=tomato_image)
timer_text=canvas.create_text(310, 320, fill="black", font="Times 20 bold", text="00:00")

# canvas.create_text(320, 450, fill="green", font="Times 30 bold", text="✔")
# canvas.create_text(360, 450, fill="green", font="Times 30 bold", text="✔")
# canvas.create_text(240, 450, fill="green", font="Times 30 bold", text="✔")

# tick_label = tkinter.Label(window, text = "✔" ,fg ="green" ,font =("Times",30))
# tick_label.grid(row=3,column=3)
start_button=Button(window, text="Start", bg="green", fg="black", font=("Times", 20), command=start_timer)
start_button.grid(row=2, column=1)
stop_button=Button(window, text="Reset", bg="green", fg="black", font=("Times", 20), command=reset_timer)
stop_button.grid(row=2, column=4)
check_marks=Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check_marks.grid(column=1, row=1)

window.mainloop()
