import numpy as np
import pandas as pd
import random

class Die():
    """This class represents a Die object. Each Die object has faces and weights that are stored in a DataFrame. The die has three attributes and three methods. The attributes are an array for face values, a list for weights that is converted to an array during initialization, and a dataframe to store the faces and weights. The first method changes the weight of a single side. The second method rolls the die a desired number of times and returns a list with the roll values. The third method shows the current state of the dataframe."""
    faces = np.array([])
    weights = []
    die_df = pd.DataFrame([])
    
    def __init__(self, faces):
        """Instantiates die object. An array is required as input argument for the faces of the die. The face array is instantiated. Test that face array is a numpy array and contains distinct values. Weights are internally initialized as 1.0 in the list then changed to an array. A dataframe is initialized with faces and weights as same length columns."""    
        self.faces = faces
        
        #Test to see if input for faces is Numpy Array
        if isinstance(self.faces,np.ndarray):
            pass
        else:
            raise TypeError("Input values for faces must be a NumPy array.")
        
        #Test to see if face values are distinct
        if len(self.faces) != np.unique(self.faces).size:
            raise ValueError("Face values must be distinct.")
        
        self.weights=[]
        for n in self.faces:
            self.weights.append(1.0)
        weights = np.array(self.weights)
        self.die_df = pd.DataFrame({'Faces':faces, 'Weights':weights})
    def change_weight_single_side(self,face_value, new_weight):
        """Changes weight of a single side of the die. This method requires two inputs: one for the associated face value to be changed and one for the new weight value. Nothing is returned."""
        
        if type(face_value) == str:
            self.die_df.loc[face_value,"Weights"]= new_weight
        elif type(face_value) == int:
            self.die_df.loc[face_value-1,"Weights"]= new_weight
        elif type(face_value) == float:
            self.die_df.loc[face_value-1,"Weights"]= new_weight
        
        #Check to see if face passed is valid value (if die is not array raise IndexError)
        if face_value not in self.faces:
            raise IndexError("Value passed is not in Faces Array")
        
        #Check to see if weight is a valid type (if not numeric or castable, raise TypeError)
        try:
            int(new_weight)
        except ValueError:
            raise TypeError("Weight value must be an int")
        
        
    def roll_die(self, num_rolls=1):
        """Rolls die desired number of times, the input argument, as a random sample with replacement with default value of one. Returns outcome as list"""
        roll_die_df = self.die_df.sample(n=num_rolls, replace=True, weights=self.die_df['Weights'])
        roll_die_list = roll_die_df['Faces'].to_list()
        return roll_die_list
            
    def show_current_state(self):
        """Shows current state of the die's private data frame. """
        print(self.die_df)

class Game():
    """This class represents the Game object. A game consists of one or more similar dice that are rolled one or more times. Similar dice have the same number of faces, but each die object may have its own weights. Each game is initialized with a list containing one or more Die objects. Games have behaviors to play , roll all dice a given number of times and return a results dataframe, and to returns the results dataframe in a wide or narrow format."""
    dice =[]
    results_df = pd.DataFrame()
    
    def __init__(self, dice):
        """Instantiates die object. A list of Die objects is required as the input argument. The results_df is not instantiated until the play method is used."""  
        self.dice = dice
     
    def play(self, num_rolls):
        """This behavior rolls all the Die objects in the dice list a given number of times using the roll method from the Die class. The number of rolls is determined by the input argument. The method returns a results dataframe with row index as roll, column index as die number, and roll values as cell."""
        self.results_df=pd.DataFrame(0, columns=np.arange(num_rolls), index=range(len(self.dice)))
        num_die=0
        while num_die < len(self.dice):
            self.results_df.loc[num_die] = self.dice[num_die].roll_die(num_rolls)
            num_die+=1
        self.results_df.index+=1
        self.results_df.columns+=1
        self.results_df = self.results_df.transpose()
        return self.results_df
    
    def show_results(self, form="wide"):
        """This method shows the results of most recent play as the results dataframe. The dataframe is formatted to be wide or narrow based on the user input. The results_df will be altered based on the input and returned and printed."""
         #Raise ValueError if user passes invalid option for narrow/wide
        if form == "wide":
            print(self.results_df)
            return self.results_df
        elif form == "narrow":
            self.results_df = self.results_df.stack()
            print(self.results_df)
            return self.results_df
        else:
            raise ValueError("Form must be entered as 'wide' or 'narrow'")
            
class Analyzer():
    """This class represents the Analyzer object. The object takes the results of a single Game object and computes descriptive statistical properties to show results of the single game. The class has a game object and list of dice as attributes and has four methods. The first method is jackpot which computes how many times the game results in the dice having the same roll value for all of the dice it returns an integer with this value. The second method is face_count which returns a dataframe with the counts for each face value across all the dice rolls. The third method, combo_count returns a dataframe with the distinct combinations and their counts (not functional). The fourth method, permutation_count returns a dataframe with distinct permutations (not functional)."""
    
    dice = []
    game = Game(dice)
    
    def __init__(self, game):
        """Instantiates analyzer object, a game object is required as an input parameter. """
        self.game = game
        #Raise ValueError if passed value is not a Game object
        if isinstance(self.game,Game):
            pass
        else:
            raise TypeError("Input values must be a Game object.")
        
    def jackpot(self):
        """This method computes how many times the game results in a jackpot, the number of times the game results in a die having the same roll value for all of its rolls. The method returns the number of jackpots as an integer."""
        num_jackpot = 0
        for row in range((self.game.results_df.shape[1])):
            indicator = []
            nums = self.game.results_df[row+1].iloc[0]
            for num in range((self.game.results_df.shape[0])):
                if self.game.results_df[row+1].iloc[num] == nums:
                    indicator.append(True)
                else:
                    continue
            if len(indicator) == len((self.game.results_df)):
                num_jackpot += 1
            else:
                continue
        return num_jackpot
    
    def face_count(self):
        """This method computes the counts of each face value for all the rolls of all the dice. The method returns a wide dataframe with the face values and their associated counts."""
        face_values = range(1,len(self.game.dice[0].faces)+1)
        face_count = [0] * len(self.game.dice[0].faces)
        face_count_df = pd.DataFrame({'Face_value':face_values, 'Face_count':face_count})
        face_count_df.set_index('Face_value', inplace=True)
        #print(face_count_df)
        for col in range(len(self.game.results_df.columns)):
            for num in range(len(self.game.results_df[col+1])):
                face_count_df.loc[self.game.results_df[col+1].iloc[num],"Face_count"]+=1
        return(face_count_df)
                
    
    def combo_count(self):
        """This method computes computations of the rolls and returns multiindex dataframe with distinct combinations and their counts""" 

    def permutation_count(self):
         """This method computes permutations of the rolls and returns multiindex dataframe with distinct permutations and their associated counts"""       
        
if __name__ == "__main__":
    import sys