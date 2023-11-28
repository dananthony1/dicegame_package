import pandas as pd

class Analyzer():
    name = ""
    email = ""
    fav_genre = "" 
    num_books = int()
    book_list = pd.DataFrame()
    
    def __init__(self, name, email, fav_genre, num_books=0,book_list=pd.DataFrame({'book_name':[],'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre=fav_genre
        self.num_books = num_books
        self.book_list = book_list
     
    def __init__(self):
        """Instantiates analyzer object, takes game object"""
        #Raise ValueError if passed value is not a Game object
    
    def jackpot():
        """computes how many times the game results in a jackpot"""
    
    def face_count():
        """Returns wide dataframe with counts for each face value"""

    def combo_count():
        """Returns multiindex dataframe with distinct combinations and their counts""" 

    def permutation_count():
         """Returns multiindex dataframe with distinct permutations and their associated counts"""