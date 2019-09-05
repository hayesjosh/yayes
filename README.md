# Yayes Data Patching

### Overview:
Yayes patching was designed to repair erroneous entries in data streams while maintaining accuracy of overall trends. In situations where users expect that missing data or data input errors might cause sudden drops in a variable values followed by immediate returns to correct variable values, yayes can be utilized. This method was inspired by the logic behind max-pooling insofar as high values of data often contain more meaningful information and that lower values of data may more often be discarded without losing relevant information. 

Yayes is not intended to resolve all data errors and should only be applied intentionally to those specific contexts where it defensibly improves subsequent analyses. 


### Example Code
```
import yayes 

df[yayes_col] = yayes(col_to_yayes)
```

### Data Patching Logic
The Yayes patcher takes in an array and calculates a difference array. The patcher then traverses the array and only activates once a negative difference occurs. If a second negative difference occurs, the walker deactivates. Otherwise, the walker continues navigating the array for as long as the values do not differ significantly. Once a significant increase is observed, the walker determines the magnitude of the increase and either marks the gap to be patched or deactivates. Patching is done by calling a separate function that applied a linear transformation between two points of the array. After patching, the walker restarts traversing the array after the point of initial activation.  
### Examples of Data Patching
- Examples of Yayes Data Patching

![Initial History](https://github.com/hayesjosh/yayes/blob/master/vis/example1/no_yayes.png)
![Completed Yayes](https://github.com/hayesjosh/yayes/blob/master/vis/example1/both.png)

![Initial History](https://github.com/hayesjosh/yayes/blob/master/vis/example2/no_yayes.png)
![Completed Yayes](https://github.com/hayesjosh/yayes/blob/master/vis/example2/both.png)

![Initial History](https://github.com/hayesjosh/yayes/blob/master/vis/example3/no_yayes.png)
![Completed Yayes](https://github.com/hayesjosh/yayes/blob/master/vis/example3/both.png)

![Initial History](https://github.com/hayesjosh/yayes/blob/master/vis/example4/no_yayes.png)
![Completed Yayes](https://github.com/hayesjosh/yayes/blob/master/vis/example4/both.png)

### Arguments and Adjustments
- Threshold Ceiling to Continue Walk
- Increases-Window to Deactive Walk 
- Return Range to Activate Patching
- Growth Floor to Activate Patching
- Final Entry Lifting On/Off
- Final Entry Lift Threshold
  
## Contact

Correspondences can be direct to gsyann@berkeley.edu and hayesjosh@alumni.stanford.edu. 