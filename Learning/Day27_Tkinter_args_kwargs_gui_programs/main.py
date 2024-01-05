from tkinter import *

def button_clicked( ):
    miles = miles_input.get( )
    km = int( miles ) * 1.6
    km_result_label.config(text=f"{km:.2f}" )
    print("Height: ", window.winfo_height( ) )
    print( "Width: ", window.winfo_width( ) )
    

window = Tk( )
window.title( "Mile to Km Converter" )
window.minsize( width=300, height=89 )

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1) 
window.grid_rowconfigure(4, weight=1) 

miles_input = Entry( )
miles_input.grid( column=1, row=0 )

miles_label = Label( text="Miles" )
miles_label.grid( column=2, row=0 )

is_equal_label = Label( text="is equal to" )
is_equal_label.grid( column=1, row=1 )

km_result_label = Label( text= "0" )
km_result_label.grid( column=1, row=2 )

km_label = Label( text="Km" )
km_label.grid( column=2, row=2 )

calculate_button = Button( text="Calculate", command=button_clicked )
calculate_button.grid( column=1, row=3 )


window.mainloop( )

print( window.winfo_width( ) )