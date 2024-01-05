import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic( "blank_states_img.gif" )

data = pandas.read_csv( "50_states.csv" )
all_states = data.state.to_list( )
guessed_states = [ ]
 
answer_state = screen.textinput( title="Guess the State", prompt="What's another state's name?" )
guessed_state = turtle.Turtle( )
guessed_state.hideturtle( )
guessed_state.penup( )
guessed_state.write( answer_state, align="center", font=("Arial", 12, "normal") )


if answer_state in all_states:
    guessed_states.append( answer_state )
    state_data = ( data[data.state == answer_state].x.iloc[ 0 ], data[data.state == answer_state].y.iloc[ 0 ] )
    guessed_state.goto( state_data[ 0 ], state_data[ 1 ] )
    answer_state = screen.textinput( title="Guess the State", prompt="What's another state's name?" )





screen.mainloop( )