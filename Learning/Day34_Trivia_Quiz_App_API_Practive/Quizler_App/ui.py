from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk( )
        self.window.title( "Quizzler" )
        self.window.config( bg=THEME_COLOR, padx=20, pady=20 )

        self.score_label = Label( text="Score: 0", fg="white", bg=THEME_COLOR, font=(15) )
        self.score_label.grid( row=0, column=1 )

        self.question_canvas = Canvas( width=300, height=250, bg="white" )
        self.question_text = self.question_canvas.create_text( 150, 125, text="Some Text", fill=THEME_COLOR, font=( "Arial", 20, "italic" ), width=290  )
        self.question_canvas.grid( row=1, column=0, columnspan=2, pady=50 )

        self.get_next_question( )

        true_image = PhotoImage( file="images/true.png" )
        false_image = PhotoImage( file="images/false.png" )
        self.true_button = Button( image=true_image, highlightthickness=0, command=self.check_answer_true )
        self.true_button.grid( row=2, column=0)
        self.false_button = Button( image=false_image, highlightthickness=0, command=self.check_answer_false )
        self.false_button.grid( row=2, column=1 )

        self.window.mainloop( )

    def get_next_question( self ):

        if( self.quiz.still_has_questions( ) == False ):
            messagebox.showinfo( title="You've completed the quiz!", message=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
        else:
            q_text = self.quiz.next_question( )
            self.question_canvas.itemconfig( self.question_text, text=q_text )

    def update_score_next_question( self ):
            self.update_score( )
            self.get_next_question( )

    def change_canvas_to_white( self ):
        self.question_canvas.config( bg="white" )
        self.update_score_next_question( )

    def check_answer_true( self ):
        self.quiz.check_answer( "True" )

        if( self.quiz.current_question.answer == "True" ):
            self.question_canvas.config( bg="green" )
        else:
            self.question_canvas.config( bg="red" )

        self.window.after( 700, self.change_canvas_to_white )

    def check_answer_false( self ):
        self.quiz.check_answer( "False" )
        if( self.quiz.current_question.answer == "True" ):
            self.question_canvas.config( bg="green" )
        else:
            self.question_canvas.config( bg="red" )

        self.window.after( 700, self.change_canvas_to_white )

    def update_score( self ):
        self.score_label.config( text=f"Score: {self.quiz.score}" )
