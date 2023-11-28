import numpy as np
import pandas as pd
import random

class Die():
    faces = np.array()
    weights = np.array()
    die_df = pd.DataFrame
    
    def __init__(self, faces=np.array, weights=np.array, die_df=pd.DataFrame):
        """Instantiates die object with provided attributes or defaults"""    
        #Test to see if values are distinct and raises a ValueError if not
        self.faces = faces
        
        if not isinstance(faces, np.array):
            raise TypeError
        
        if num_faces != np.unique(faces).size:
            raise ValueError
            
        self.weights = weights
        for n in len(faces):
            weights.append(1)
        
        self.die_df = die_df
        die_df = pd.DataFrame({'Faces':faces, 'Weights':weights})
     
    def change_weight_single_side(face_value, new_weight):
        """Changes weight of a single side of the die"""
        #Check to see if face passed is valid value (if die is not array raise IndexError)
        if face_value is not in faces:
            raise IndexError
        #Check to see if weight is a valid type (if not numeric or castable, raise TypeError)
        if not isinstance(int(new_weight), int):
            raise TypeError
        die_df[face_value] = new_weight
    
    def roll_die(num_rolls=1):
        """Rolls die desired number of times as a random sample with replacement with default value of one. Returns outcome as list"""
    return die_df['Faces'].sample(num_rolls, replace=True, weights='Weights')
    
    def show_current_state(die_df):
        """Shows current state of the die's private data frame"""
    print(die_df)
    
                            
