from game import Game
import unittest

class GameTestSuite(unittest.TestCase):
    """This is a docstring"""
    
    def test_1_add_book(self): 
        """Add a book and test if it is in book_list."""
        assertIn("Harry Potter and the Prizoner of Azkaban", add_book("Harry Potter and the Prizoner of Azkaban", 4),"Harry Potter is not included")
            
    def test_2_add_book(self): 
        """Add the same book twice. Test if it's in book_list only once."""
        try:
            add_book("Harry Potter and the Prizoner of Azkaban", 4)
            add_book("Harry Potter and the Prizoner of Azkaban", 4)
        except IncludedError:
            print("That book is already in book_list!")
            
    def test_3_has_read(self): 
        """Pass a book in the list and test the answer is True."""
        assertTrue(has_read("Dune"))
        
    def test_4_has_read(self): 
        """Pass a book NOT in the list and use assert False to test if the answer is True"""
        self.assertFalse(has_read("Do androids dream of electric sheep?"))
            
    def test_5_num_books_read(self): 
        """Add some books to the list, and test num_books matches expected."""
        self.assertEqual(add_book("Harry Potter and the Prizoner of Azkaban", 4),1)
        
    def test_6_fav_books(self): 
        """Add some books with ratings to the list, making sure some of them have rating > 3. Your test should check that the returned books have rating > 3."""
        try:
            add_book("Harry Potter and the Prizoner of Azkaban", 4)
            add_book("Dune", 2)
            fav_books()
        except RatingError:
            print("There is an error in the ratings!")
            
        
    if __name__ == '__main__':
        unittest.main(verbosity=3)