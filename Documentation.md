# Description
Python Library to automate the creation and analysis of PonitusMatrix.

# Usage
pd_table_func = testpontipy2(df)

## contingency_table()
### Arguments
display(pd_table_func.contingency_table())


## size() 
Function to Compute Size for all or one Category k  
Axis must be specified when category k is specified  
Determines if row or column sum for category k will be returned  
### Arguments
No category specified = Size of extent  
Category k specified = Size of category k  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) Axis 'X' = Size of category k in X (row sum)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) Axis 'Y' = Size of category k in Y (col sum)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c) No Axis specified = Size of category k  
### Example
a)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input:  print('Size of Extent:', pd_table_func.size(), 'Hectares')  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output: Size of Extent: 25662 Hectares  
b)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input:  print('Size of Category 1 in X:', pd_table_func.size(0,'X'),'Hectares')  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output: Size of Category 1 in X: 2296 Hectares  
c)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input:  print('Size of Category 1 in Y:', pd_table_func.size(0,'Y'),'Hectares')  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output: Size of Category 1 in Y: 2144 Hectares  


## difference()
Function to compute difference for all or one category
### Arguments
No category specified = Total Size - Hits  
Category K specified = Size-*(2*Hits) For That Category  
### Example


## Hits
Functions to compute Hits, Misses, and False Alarms
### Arguments
No Category specified = Sum of Total Hits, Misses, or False Alarms  
Category k specified = Hits, Misses, or False Alarms for Category k
### Example
inputs:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('Total Hits:', pd_table_func.hits(), 'Hectares')  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('Total Misses:', pd_table_func.miss(), 'Hectares')  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('The Total False Alarms:', pd_table_func.false_alarm(), 'Hectares')  

outputs:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Hits: 3553 Hectares  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Misses: 8735 Hectares  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Total False Alarms: 8735 Hectares  



## Miss
### Arguments





## false
### Arguments



## Quantity
### Arguments


## Exchange
###Arguments


## Shift
### Arguments










# Available Metrics for further computations






# Acknowledgements

Dr. Robert Gilmore Pontius Jr created the first version of this workbook in 2001. Pontius has revised this workbook several times, and each revision has a larger number for the suffix of the filename. Pontius created version 42 in 2019.

Visit www.clarku.edu/~rpontius for publications on this workbook's methods. Specificaly, see:
Pontius Jr, Robert Gilmore and Ali Santacruz. 2014. Quantity, Exchange and Shift Components of Differences in a Square Contingency Table. International Journal of Remote Sensing 35(21): 7543-7554.

Pontius Jr, Robert Gilmore. 2019. Component intensities to relate difference by category with difference overall. International Journal of Applied Earth Observations and Geoinformation 77: 94-99.

Pontius Jr, Robert Gilmore and Marco Millones. 2011. Death to Kappa: birth of quantity disagreement and allocation disagreement for accuracy assessment. International Journal of Remote Sensing 32(15): 4407-4429. 

Aldwaik, Safaa Zakaria, Jeffrey A Onsted, and Robert Gilmore Pontius Jr. 2015. Behavior-based aggregation of land categories for temporal change analysis. International Journal of Applied Earth Observation and Geoinformation 35(Part B): 229-238.
