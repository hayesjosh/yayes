# Yayes Data Patching

### Overview:
Yayes patching was designed to repair erroneous entries in data streams while maintaining accuracy of overall trends. In situations where users expect that missing data or data input errors might cause sudden drops in a variable values followed by immediate returns to correct variable values, yayes can be utilized. This method was inspired by the logic behind max-pooling insofar as high values of data often contain more meaningful information and that lower values of data may more often be discarded without losing relevant information. 

Yayes is not intended to resolve all data errors and should only be applied intentionally to those specific contexts where it defensibly improves subsequent analyses. 

### Data Patching Logic
The Yayes patcher takes in an array and calculates a difference array. The patcher then traverses the array and only activates once a negative difference occurs. If a second negative difference occurs, the walker deactivates. Otherwise, the walker continues navigating the array for as long as the values do not differ significantly. Once a significant increase is observed, the walker determines the magnitude of the increase and either marks the gap to be patched or deactivates. Patching is done by calling a separate function that applied a linear transformation between two points of the array. After patching, the walker restarts traversing the array after the point of initial activation.  

### Arguments and Adjustments
- Threshold Ceiling to Continue Walk
- Increases-Window to Deactive Walk 
- Return Range to Activate Patching
- Growth Floor to Activate Patching
- Final Entry Lifting On/Off
- Final Entry Lift Threshold

### Examples of Data Patching
- Successful Example of Yayes

- Activation:
   - Negative
   
- Deactivation Conditions:
   - Two Negatives
   - Negative Followerd by Medium Increase

- Patching Conditions: 
   - Immediate spike and return 
   - Long trough
  
## Contact

Correspondences can be direct to gsyann@berkeley.edu and hayes@ucdavis.edu. 