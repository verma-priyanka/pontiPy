![image](images/logo.PNG "Logo")

# Description
Python Library to automate the creation and analysis of PonitusMatrix.  
Version 1.2  
Python 3.7  
December, 2019  

# Dependencies & Usage
```python
import numpy as np
import pandas as pd
```

```python
pd_table_func = testpontipy2(df)
```

# Functions
Available functions in library
## contingency_table()
#### Arguments
#### Example
```python
df = pd.read_csv('sample.csv', index_col= 0)
display(df)
```
![image](images/preCSV.PNG "Dataframe")


```python
display(pd_table_func.contingency_table())
```
![image](images/postCSV.PNG "Contingency Table")



## size() 
- Function to Compute Size for all or one Category k  
- Axis must be specified when category k is specified  
- Determines if row or column sum for category k will be returned  
#### Arguments
- No category specified = Size of extent  
- Category k specified = Size of category k  
a) Axis 'X' = Size of category k in X (row sum)  
b) Axis 'Y' = Size of category k in Y (col sum)  
c) No Axis specified = Size of category k  
#### Example
```python
print('Size of Extent:', pd_table_func.size(), 'Hectares') 
```
>> _Size of Extent: 25662 Hectares_  

```python
print('Size of Category 1 in X:', pd_table_func.size(0,'X'),'Hectares')  
```
>> _Size of Category 1 in X: 2296 Hectares_  

```python
print('Size of Category 1 in Y:', pd_table_func.size(0,'Y'),'Hectares')
```
>> _Size of Category 1 in Y: 2144 Hectares_  


## difference()  
- Function to compute difference for all or one category
#### Arguments
- No category specified = Total Size - Hits  
- Category K specified = Size-*(2*Hits) For That Category  
#### Example


## hits(), miss(), false_alarm()
- Functions to compute Hits, Misses, and False Alarms
#### Arguments
- No Category specified = Sum of Total Hits, Misses, or False Alarms  
- Category k specified = Hits, Misses, or False Alarms for Category k
#### Example
```python
print('Total Hits:', pd_table_func.hits(), 'Hectares')  
```
>> _Total Hits: 3553 Hectares_  

```python
print('Total Misses:', pd_table_func.miss(), 'Hectares')  
```
>> _Total Misses: 8735 Hectares_  

```python
print('The Total False Alarms:', pd_table_func.false_alarm(), 'Hectares')  
```
>> _The Total False Alarms: 8735 Hectares_  


## quantity()
#### Arguments


## exchange    
Function to compute Exchange between ALL, ONE or TWO categories  
- 1. If no category is specified (Total must be false):  
>> Sum of total exchange is returned  
- 2. If total is False and 1 category is specified:  
>> Return is exchange for that category with all other categories + a total value in dict  
- 3. If Total is True and 1 category is specified:  
>> Return is total exchange for that category  
- 4. If 2 categories are specified (Total must be false):  
>> Return exchange between 2 categories  
#### Arguments


## shift()
#### Arguments










# Available Metrics
See Metrics that Make a Difference, Chapter 4
Link to Chapter 4

# Acknowledgements

_Dr. Robert Gilmore Pontius Jr created the first version of this workbook in 2001. Pontius has revised this workbook several times, and each revision has a larger number for the suffix of the filename. Pontius created version 42 in 2019._  

_Visit www.clarku.edu/~rpontius for publications on this workbook's methods. Specificaly, see:
Pontius Jr, Robert Gilmore and Ali Santacruz. 2014. Quantity, Exchange and Shift Components of Differences in a Square Contingency Table. International Journal of Remote Sensing 35(21): 7543-7554._  

_Pontius Jr, Robert Gilmore. 2019. Component intensities to relate difference by category with difference overall. International Journal of Applied Earth Observations and Geoinformation 77: 94-99._  

_Pontius Jr, Robert Gilmore and Marco Millones. 2011. Death to Kappa: birth of quantity disagreement and allocation disagreement for accuracy assessment. International Journal of Remote Sensing 32(15): 4407-4429._  

_Aldwaik, Safaa Zakaria, Jeffrey A Onsted, and Robert Gilmore Pontius Jr. 2015. Behavior-based aggregation of land categories for temporal change analysis. International Journal of Applied Earth Observation and Geoinformation 35(Part B): 229-238._
