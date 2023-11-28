import pandas as pd
from die import Die

class Game():
    dice =[]
    
    def __init__(self, dice):
        """Instantiates game object"""
        self.dice = dice
     
    def play(num_rolls):
        """Returns dataframe with row index as roll, column index as die number, and roll values as cell"""
    for n in dice:
        results_df = roll_die(dice[num_rolls])

    def show_results(format):
        """Shows results of most recent play"""
         #Raise ValueError if user passes invalid option for narrow/wide
    
    def add_book(book_name, rating):                             
        if(book_name.isin(book_list['book_list'])):
            print(str(book_name) + "is in the book list already!")
            raise(IncludedError)
        else:                                                                                
            book_list['book_name'].append(book_list)
            
    def has_read(book_name):
        if(book_name.isin(book_list['book_list'])):
            return True
        else:                                                                                
            return False 
                          
    def num_books_read():
        return(len(book_list.index))
    
    def fav_books():
        book_list.loc[book_list['book_list'] > 3]
        if(min(book_list['book_list'])>3):
            return True
        else:
            raise RatingError
            return False