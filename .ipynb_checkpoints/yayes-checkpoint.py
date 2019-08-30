import numpy as np
import pandas as pd

def yayes(col, X = .15, last_day = False):
    
    #Don't need?
    if type(col) == pd.Series:
        col = col.values
    col = col.astype('float32')
    differences = np.diff(col)
    max_i = len(differences)    

    for i in range(len(col)-2):
        
        current_diff = differences[i]
        next_diff = differences[i+1]
        
        if current_diff >= 0 and next_diff < 0:
            
            j = i + 2
            
            max_diff_threshold = next_diff
            
            while j < max_i and (0 <= differences[j] <= abs(max_diff_threshold * X)):
                
                j += 1
                
            if j < max_i and differences[j] > (.5*max_diff_threshold) and differences[j] > 0:
                fill_value = col[i+1]
                increase = (col[j+1] - col[i+1]) / (j - i)
                
                k, x = i + 2, 1
                
                while k <= j:
                    col[k] = fill_value + (increase * x)
                    k,x = k+1, x+1
                    
                differences = np.diff(col)
    return col        