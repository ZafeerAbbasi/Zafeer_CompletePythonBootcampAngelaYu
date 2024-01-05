import pandas 

#Colors: Gray, Black, Cinnamon
#Goal: Find the number of squirrels per color

data = pandas.read_csv( "2018_Central_Park_Squirrel_Census__Squirrel_Data_20231231.csv" )

num_gray_squirrels = len( data[ data["Primary Fur Color"] == "Gray" ] )
num_black_squirrels = len( data[ data["Primary Fur Color"] == "Black" ] )
num_cinnamon_squirrels = len( data[ data["Primary Fur Color"] == "Cinnamon" ] )

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [num_gray_squirrels, num_black_squirrels, num_cinnamon_squirrels]
}

df = pandas.DataFrame( data_dict )