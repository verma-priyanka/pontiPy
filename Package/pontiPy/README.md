pontiPy: A Python Library for Map Comparison Metrics in a Cross-Tab Matrix
Latest Version: 3.0
Latest Update: October 2021
Python Version: 3.7  

Documentation: https://github.com/verma-priyanka/pontiPy

# Dependencies & Usage
- Download: pip install -i pontiPy==3.0
- Required libraries for pontiPy usage

```python
import pandas as pd
from pontiPy import pontiPy
```
- Creating a Dataframe from an inputted Sample & Loading the pontiPy package
```python
df = pd.read_csv('sample.csv', index_col= 0)
display(df)
pontipy_df = pontiPy(df)
```

# Further Information & Contact
- **Library Information:**  
Priyanka Verma, prverma@clarku.edu
Priscilla Ahn, pahn@clarku.edu    

- **Metric Methodolgy:**  
Robert (Gil) Pontius, rpontius@clarku.edu  
See Metrics that Make a Difference, Chapter 4  
Link to Chapter 4

# Acknowledgements

_Dr. Robert Gilmore Pontius Jr created the first version of this workbook in 2001. Pontius has revised this workbook several times, and each revision has a larger number for the suffix of the filename. Pontius created version 42 in 2019._  

_Visit www.clarku.edu/~rpontius for publications on this workbook's methods. Specificaly, see:
Pontius Jr, Robert Gilmore and Ali Santacruz. 2014. Quantity, Exchange and Shift Components of Differences in a Square Contingency Table. International Journal of Remote Sensing 35(21): 7543-7554._  

_Pontius Jr, Robert Gilmore. 2019. Component intensities to relate difference by category with difference overall. International Journal of Applied Earth Observations and Geoinformation 77: 94-99._  

_Pontius Jr, Robert Gilmore and Marco Millones. 2011. Death to Kappa: birth of quantity disagreement and allocation disagreement for accuracy assessment. International Journal of Remote Sensing 32(15): 4407-4429._  

_Aldwaik, Safaa Zakaria, Jeffrey A Onsted, and Robert Gilmore Pontius Jr. 2015. Behavior-based aggregation of land categories for temporal change analysis. International Journal of Applied Earth Observation and Geoinformation 35(Part B): 229-238._
