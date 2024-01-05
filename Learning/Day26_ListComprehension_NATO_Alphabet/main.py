import pandas

data = pandas.read_csv( "nato_phonetic_alphabet.csv" )

# for key,item in data.iterrows( ):
#     print( item )

# user_input = input( "Enter a letter: " ).upper( )

# user_input = 'A'

# answer = [ item.code for ( key, item ) in data.iterrows( ) if item.letter == user_input ]
# print( type( answer ) )

new_dict = { item.letter:item.code for ( index, item ) in data.iterrows( ) }
user_input = input( "Enter a word: " ).upper( )

# new_list = [ word for letter in user_input for (letter1, word) in new_dict.items( ) if letter1 == letter ]
new_list = [ new_dict[ letter ] for letter in user_input ]

print( new_list )