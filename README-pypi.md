# Yayes Data Patching

### Overview:
Yayes patching was designed to repair erroneous entries in data streams while maintaining accuracy of overall trends. The yayes package is most powerful in situations where users see sudden, temporary drops in variables' values that then return to correct variable values (i.e. discrepancies in variable values that may be caused by missing data or data input errors). This method was inspired by the logic behind max-pooling insofar as high values of data often contain more meaningful information and that lower values of data may more often be discarded without losing relevant information. 

Yayes is not intended to resolve all data errors and should only be applied intentionally to those specific contexts where it defensibly improves subsequent analyses. 


### Example Code

> import yayes 

> df[yayes_col] = yayes(col_to_yayes)


#### Inputs:
    
* x: a pandas Series or numpy array on which yayes will be applied.
        
* continue_walk_thresh: a float between 0 and 1 that determines whether to continue walking along trough or not.  If the function sees an increase that is larger than continue_walk_thresh * (the initial difference that triggered the process), the walk stops.
                              
* max_walk_range: an (optional) integer > 0 that stops the walking process if the function has traversed at least max_walk_range steps.
        
* final_entry_lift: a boolean that determines whether whether to apply the yayes process to the last entry in the array.
        
* final_entry_lift_thresh: a float between 0 and 1.  If final_entry_lift_thresh * (the second to last value in the array) is greater than or equal to the amount
                                 dropped at the final entry, apply the yayes process.
    
#### Output:

* x: The input (numpy) array after the yayes process has been applied

### Data Patching Logic
The Yayes patcher takes in an array and calculates a difference array. The patcher then traverses the array and only activates once a negative difference occurs. If a second negative difference occurs, the walker deactivates. Otherwise, the walker continues navigating the array for as long as the values do not differ significantly. Once a significant increase is observed, the walker determines the magnitude of the increase and either marks the gap to be patched or deactivates. Patching is done by calling a separate function that applied a linear transformation between two points of the array. After patching, the walker restarts traversing the array after the point of initial activation.  

  
## Contact

Correspondences can be direct to gsyann@berkeley.edu and hayesjosh@alumni.stanford.edu. 