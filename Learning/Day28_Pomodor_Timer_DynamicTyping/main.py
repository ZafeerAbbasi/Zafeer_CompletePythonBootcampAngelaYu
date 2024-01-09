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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def start_timer( ):
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1

    #If its the  


    


    count_down( num_sec_duration )

# Function to update time
def count_down( sec ):
    count_min = math.floor( sec / 60 )
    if( sec >= 0 ):
        count_sec = sec % 60 
    else:
        count_sec = 0

    canvas.itemconfig( time_label, text = f"{0:02d}:{count_sec:02d}" )
    if( sec >= 0 ):
        window.after( 1000, count_down, sec - 1 )
    else:
        window.title( "Done" )
# ---------------------------- UI SETUP ------------------------------- #

window = Tk( )
window.title( "Pomodoro" )
window.config( padx=25, pady=25, bg=YELLOW )

# Label 
main_label = Label( text="Pomodoro Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold") )
main_label.grid( column=1, row=0 )

canvas = Canvas( width=200, height=224, bg=YELLOW, highlightthickness=0 )
tomato_img = PhotoImage( file="tomato.png" )
canvas.create_image( 100, 112, image=tomato_img )
time_label = canvas.create_text( 100, 130, text="0", fill="white", font=(FONT_NAME, 35, "bold") )
canvas.grid( column=1, row=1 )

# Reset Button
reset_button = Button( text="Reset", highlightthickness=0 )
reset_button.grid( column=2, row=2 )

# Checkmark Label
checkmark_label = Label( text="✔", fg='#000000', bg=YELLOW )
checkmark_label.grid( column=1, row=3 )

# Start Button
start_button = Button( text="Start", highlightthickness=0, command=start_timer )
start_button.grid( column=0, row=2 )

window.mainloop( )