# Description
Python Library to automate the creation and analysis of PonitusMatrix.

# Usage
pd_table_func = testpontipy2(df)

## contingency_table()
### Arguments
display(pd_table_func.contingency_table())


## size() 
### Arguments
No category specified = Size of extent
Category k specified = Size of category k
  a) Axis 'X' = Size of category k in X (row sum)
  b) Axis 'Y' = Size of category k in Y (col sum)
  c) No Axis specified = Size of category k
### Example
a)
input:  print('Size of Extent:', pd_table_func.size(), 'Hectares')
output: Size of Extent: 25662 Hectares
b)
input:  print('Size of Category 1 in X:', pd_table_func.size(0,'X'),'Hectares')
output: Size of Category 1 in X: 2296 Hectares
c)
input:  print('Size of Category 1 in Y:', pd_table_func.size(0,'Y'),'Hectares')
output: Size of Category 1 in Y: 2144 Hectares




## difference()
### Arguments



## Hits
### Arguments




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
