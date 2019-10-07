import numpy as np
import pandas as pd

def yayes(x, continue_walk_thresh = .15, max_walk_range=None, final_entry_lift = False, final_entry_lift_thresh=.95):
    
    """
    Inputs:
    
        x: a pandas Series or numpy array on which yayes will be applied.
        
        continue_walk_thresh: a float between 0 and 1 that determines whether to continue walking along trough or not.  If the function sees an increase that is larger than
                              continue_walk_thresh * (the initial difference that triggered the process), the walk stops.
                              
        max_walk_range: an (optional) integer > 0 that stops the walking process if the function has traversed at least max_walk_range steps.
        
        final_entry_lift: a boolean that determines whether whether to apply the yayes process to the last entry in the array.
        
        final_entry_lift_thresh: a float between 0 and 1.  If final_entry_lift_thresh * (the second to last value in the array) is greater than or equal to the amount
                                 dropped at the final entry, apply the yayes process.
    
    Output:
        x: The input (numpy) array after the yayes process has been applied
    """
    
    if type(x) == pd.Series:
        x = x.values
    x = x.astype('float64')
    differences = np.diff(x)
    max_i = len(differences)    

    for i in range(len(x)-2):
        
        current_diff = differences[i]
        next_diff = differences[i+1]
        
        if current_diff >= 0 and next_diff < 0:
            
            j = i + 2
            
            max_diff_threshold = next_diff
            
            steps=0
            
            while j < max_i and (0 <= differences[j] <= abs(max_diff_threshold * continue_walk_thresh)):
                
                j += 1
                steps+=1
            
            if max_walk_range and steps >= max_walk_range:
                continue
                
            if j < max_i and differences[j] > (.5*max_diff_threshold) and differences[j] > 0:
                fill_value = x[i+1]
                increase = (x[j+1] - x[i+1]) / (j - i)
                
                k, c = i + 2, 1
                
                while k <= j:
                    x[k] = fill_value + (increase * c)
                    k,c = k+1, c+1
                    
                differences = np.diff(x)

    if final_entry_lift:
        last_val = x[len(x)-1]
        second_last_val = x[len(x)-2]
        last_diff = differences[max_i-1]
        if -last_diff > final_entry_lift_thresh*second_last_val:
            x[len(x)-1] = second_last_val
        
    return x           