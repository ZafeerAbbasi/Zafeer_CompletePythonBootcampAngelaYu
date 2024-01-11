import smtplib
import random
import datetime as dt

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

my_email = "w56454415@gmail.com"
my_password = "rhkt jzog yqfv tsqt"

# Get current day
current_day = dt.datetime.now( ).weekday( )

if( current_day == WEDNESDAY ):

    with open( file="quotes.txt" ) as file:
        quote = random.choice( file.readlines( ) )

        with smtplib.SMTP( host="smtp.gmail.com", port=587 ) as connection:
            connection.starttls( )
            connection.login( user=my_email, password=my_password )
            connection.sendmail( 
                from_addr=my_email, 
                to_addrs="wealthyviewz@gmail.com", 
                msg=f"Subject:Quote of the Day\n\n{ quote }" )