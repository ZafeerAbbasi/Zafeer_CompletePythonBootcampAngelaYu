BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random


current_index_dict = { }

# ----------------- Accessing Data ----------------- 
dataframe = pandas.read_csv( filepath_or_buffer="data/french_words.csv" )
data_dict = dataframe.to_dict( orient="records" )

# ------------------ Switching Card Sides -----------

def switch_to_back( ):
    global current_french_word
    my_canvas.itemconfig( flash_card, image=card_back )
    my_canvas.itemconfig( top_text, fill="#FFFFFF", text="English" )
    my_canvas.itemconfig( bottom_text, fill="#FFFFFF", text=current_index_dict["English"])

def switch_to_front( ):
    global current_french_word
    my_canvas.itemconfig( flash_card, image=card_front )
    my_canvas.itemconfig( top_text, fill="#000000", text="French" )
    my_canvas.itemconfig( bottom_text, fill="#000000", text=get_random_secondary_word( ) )
    window.after( 3000, switch_to_back )

def got_it_right( ):
    data_dict.remove( current_index_dict )
    new_df = pandas.DataFrame( data_dict )
    new_df.to_csv( "words_to_learn.csv" )
    switch_to_front( )



#---------------- Button Commands ------------------

def get_random_secondary_word( ):
    index_dict = random.choice( data_dict ) 
    global current_index_dict 
    current_index_dict = index_dict 
    return index_dict[ "French"]
    

#---------------- UI ------------------------------

window = Tk( )
window.title( "Flashy" )
window.config( bg=BACKGROUND_COLOR, padx=50, pady=50 )
window.after( 3000, switch_to_back )

card_front = PhotoImage( file="images/card_front.png", height=526, width=800 )
card_back = PhotoImage( file="images/card_back.png" )
right_image = PhotoImage( file="images/right.png" )
wrong_image = PhotoImage( file="images/wrong.png" )

my_canvas = Canvas( width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0 )
flash_card = my_canvas.create_image(400, 265, image=card_front )
top_text = my_canvas.create_text( 400, 150, text="French", font=( "Ariel", 40, "italic" ) )
bottom_text = my_canvas.create_text( 400, 263, text=get_random_secondary_word( ), font=( "Ariel", 60, "bold" ) )
my_canvas.grid( row=0, column=0, columnspan=2, pady=20 )

right_btn = Button( image=right_image, highlightthickness=0, command=got_it_right )
right_btn.grid( row=1, column=1 )
wrong_btn = Button( image=wrong_image, highlightthickness=0 )
wrong_btn.grid( row=1, column=0 )






window.mainloop( )