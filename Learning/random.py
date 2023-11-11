"""_summary_
"""

def mutate_me( a_list ):
    """_summary_

    Args:
        a_list (_type_): _description_
    """
    b_list = [ ]
    for item in a_list:
        new_item = item * 2
        b_list.append( new_item )
    print( b_list )


mutate_me( [ 1, 2, 3, 5, 8, 13 ] )
