from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import unittest

class DieTestSuite(unittest.TestCase):
    """Test suite for die methods"""
    def test_1_change_weight_single_side(self): 
        #Test to see if weight of corresponding face value changes
        Die1 = Die(faces=np.array(1,2,3,4))
        Die1.change_weight_single_side(1,2)
        face1 = self.die_df.loc[0]
        #error message in case the test fails
        message = "The weight for face 1 is not 2."
        self.assertTrue(face1=2, message) 
        
    def test_2_roll_die(self): 
        #Test to see if roll die returns a list the length of num_rolls
        Die1 = Die(faces=np.array(1,2,3,4))
        Die1.roll_die(2)
        list_length = len(self.Die1.roll_die_list)
        
        message = "The list length is not 2."
        self.assertTrue(list_length = 2, message)
        
    def test_3_show_current_state(self): 
        #Check to see if the type of the die_df is a dataframe
        Die1 = Die(faces=np.array(1,2,3,4))
        Die1.show_current_state()
        df = type(self.Die1.die_df)
        message = "The type of die_df is not a DataFrame" 
        self.assertTrue(df = pd.DataFrame(), message)
            
class GameTestSuite(unittest.TestCase):
    """Test suite for game methods"""
    def test_4_play(self): 
        #Test to see if the results dataframe has a size of 2
        Die1 = Die(faces=np.array(1,2,3,4))
        Game1 = Game([Die1])
        results = Game1.play(2)
        size = results.size()
        #error message in case the test fails
        message = "The size of the results data frame is not 2"
        self.assertTrue(size=2, message) 
        
    def test_5_show_results(self): 
        """Check that the face values are unique.""" 
        #Test to see if the results dataframe has a size of 2
        Die1 = Die(faces=np.array(1,2,3,4))
        Game1 = Game([Die1])
        results1 = Game1.show_results()
        size1 = results1.size()
        results2 = Game1.show_results('narrow')
        size2 = results2.size()
        #error message in case the test fails
        message = "The size of the results data frames are not equal"
        self.assertEqual(size1=size2, message) 

class AnalyzerTestSuite(unittest.TestCase):
    """Test suite for analyzer methods"""
    def test_6_jackpot(self): 
       #Test to see if the results dataframe has a size of 2
        Die1 = Die(faces=np.array(1,2,3,4))
        Game1 = Game([Die1])
        Analyzer1 = Analyzer(Game1)
        num = Analyzer1.jackpot()
        integer = type(num) 
        #error message in case the test fails
        message = "The type of the return value is not an integer"
        self.assertEqual(integer=int, message)  
        
    def test_7_face_count(self): 
        #Test to see if the results dataframe has a size of 2
        Die1 = Die(faces=np.array(1,2,3,4))
        Game1 = Game([Die1])
        results = Game1.play(2)
        size = results.size()
        #error message in case the test fails
        message = "The size of the results data frame is not 2"
        self.assertTrue(size=2, message)                     
        
    def test_8_combo_count(self): 
        
    def test_9_permutation_count(self): 
        
    if __name__ == '__main__':
        unittest.main(verbosity=3)