# with open( "LearningFiles/my_file.txt" ) as file:
#     contents = file.read( )
#     print( contents )

with open( file="LearningFiles/my_file.txt", mode="a") as file:
    file.write( "\nNew text." )