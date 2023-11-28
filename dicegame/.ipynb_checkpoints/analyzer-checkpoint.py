import pandas as pd

class BookLover():
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