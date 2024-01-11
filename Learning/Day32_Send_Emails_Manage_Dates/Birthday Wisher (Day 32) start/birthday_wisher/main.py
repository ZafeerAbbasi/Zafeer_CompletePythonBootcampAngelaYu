##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

LETTERS = [ "letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt" ]
my_email = "w56454415@gmail.com"
my_password = "rhkt jzog yqfv tsqt"

today_month_day = ( dt.datetime.now( ).month, dt.datetime.now( ).day )

birthday_names_months_days = list( zip(
    pandas.read_csv( filepath_or_buffer="birthdays.csv" ).to_dict( orient="list" )["name"],
    pandas.read_csv( filepath_or_buffer="birthdays.csv" ).to_dict( orient="list" )["month"],
    pandas.read_csv( filepath_or_buffer="birthdays.csv" ).to_dict( orient="list" )["day"]
) )

birthday_months_days = [ ( index[1], index[2] ) for index in birthday_names_months_days ]

if today_month_day in birthday_months_days:
    letter = random.choice( LETTERS )
    person = birthday_names_months_days[ birthday_months_days.index( today_month_day ) ][ 0 ]

    with open( file=letter, mode="r" ) as file:
        content = file.read( )
        content = content.replace( "[NAME]", person )
    
    with smtplib.SMTP( host="smtp.gmail.com", port=587 ) as connection:
        connection.starttls( )
        connection.login( user=my_email, password=my_password )
        connection.sendmail( 
            from_addr=my_email,
            to_addrs="wealthyviewz@gmail.com",
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )
    




