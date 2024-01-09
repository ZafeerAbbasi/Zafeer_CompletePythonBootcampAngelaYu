from tkinter import *
from tkinter import messagebox
from password_gen import generate_password
import pyperclip
import json
NORM_FONT= ("Verdana", 10)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def add_generated_password( ):
    generated_password = generate_password( )
    password_entry.delete( 0, END )
    password_entry.insert( 0, generated_password)
    #Copy generated password to clipboard
    pyperclip.copy(generated_password)

def find_password( ):
    output = ""
    website_to_check = website_entry.get( ).lower( )
    try: 
        with open(file="passwords_data.json", mode="r" ) as file:
            data = json.load( file )
    except ( FileNotFoundError, json.decoder.JSONDecodeError ):
        output = "No Data File Found."
        messagebox.showerror( title="ERROR", message=output )
    else:
        websites = [ website.lower( ) for website in data ]
        if website_to_check in websites:
            email = [ data[website]["email"] for website in data if website == website_to_check ][0]
            password = [ data[website]["password"] for website in data if website == website_to_check ][0]
            output = f"{'Email:          '}{email}\n{'Password:   '}{password}"
            print( output )
        else:
            output = f"No details for {website_to_check} exists."
        messagebox.showinfo( title=website_to_check, message=output)
        

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data( ):
    #Save data to file
    website_data = website_entry.get( )
    email_username_data = email_username_entry.get( )
    password_data = password_entry.get( )
    new_data = {
        website_data: {
            "email": email_username_data,
            "password" : password_data,
        }
    }

    if( len( website_data ) == 0 ):
        messagebox.showerror( title="ERROR", message="Please enter a valid website." )
    elif( len( email_username_data ) == 0 ):
        messagebox.showerror( title="ERROR", message="Please enter a valid Email/Username." )
    elif( len( password_data ) == 0 ):
        messagebox.showerror( title="ERROR", message="Please enter a valid password." )
    else:
        try: 
            with open(file="passwords_data.json", mode="r" ) as file:
                data = json.load( file )
        except ( FileNotFoundError, json.decoder.JSONDecodeError ):
            with open( file="passwords_data.json", mode="w" ) as file:
                json.dump( new_data, file, indent=4 )
        else:
            data.update( new_data )
            with open( file="passwords_data.json", mode="w" ) as file:
                json.dump( data, file, indent=4 )
        finally:
            #Clear current entry data
            website_entry.delete( 0, END )
            password_entry.delete( 0, END )
 
# ---------------------------- UI SETUP ------------------------------- # 

window = Tk( )
window.title( "Password Manager" )
window.config( padx=20, pady=20 )

my_canvas = Canvas( height=200, width=200 )
my_image = PhotoImage( file="logo.png" )
canvas_image_lock = my_canvas.create_image( 100, 100, image=my_image )
my_canvas.grid( row=0, column=1 )

#Labels
website_label = Label( text="Website: " )
website_label.grid( row=1, column= 0 )

email_username_label = Label( text="Email/Username: " )
email_username_label.grid( row=2, column=0 )

password_label = Label( text="Password: " )
password_label.grid( row=3, column=0 )

#Entries
website_entry = Entry(  )
website_entry.grid( row=1, column=1, columnspan=2, sticky="EW" )
website_entry.focus( )

email_username_entry = Entry( )
email_username_entry.grid( row=2, column=1, columnspan=2, sticky="EW" )
email_username_entry.insert( 0, "zafeerabbasi57@yahoo.com" )

password_entry = Entry( )
password_entry.grid( row=3, column=1, sticky="EW" )

#Buttons
generate_password_button = Button( text="Generate Password", command=add_generated_password )
generate_password_button.grid(row=3, column=2, sticky="EW" )

add_button = Button( width=35, text="Add" )
add_button.grid( row=4, column=1, columnspan=2, sticky="EW" )
add_button.config( command=save_data )

search_button = Button( text="Search", command=find_password )
search_button.grid( row=1, column=2, sticky="EW" )





window.mainloop( )