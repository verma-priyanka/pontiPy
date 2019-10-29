# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:40:21 2019

@author: JFrey
"""

import numpy as np
import pandas as pd
import csv

#contingency = np.matrix([[7, 2, 0, 1],
#        [1, 7, 2, 0],
#        [0, 1, 7, 2],
#        [2, 0, 1, 7]])


#file path:
# E:/OneDrive/Documents/School_Work/Clark/Map_Comparison/final_proj/PontiusMatrix/Data/contingency.csv

my_path = input("Enter the file path: ")

# find the number of columns in csv
with open(my_path) as f:
    ncols = len(f.readline().split(',')) #comma delimited

# load in csv, skipping first row and column
contingency_table = np.loadtxt(open(my_path, "rb"), 
                               delimiter = ",", 
                               skiprows = 1,
                               usecols = range(1, ncols))
print(contingency_table)


#find sum of hits:
total_hits = 0
for i in range(0, ncols-1):
    total_hits = total_hits + contingency_table[i,i]
print(total_hits)
    

#find column sums
column_totals = np.array([])
for i in range(0, ncols-1):
    column_totals = np.append(column_totals, sum(contingency_table[:,i]))
print(column_totals)

# find row totals:
row_totals = np.array([])
for i in range(0, ncols-1):
    row_totals = np.append(row_totals, sum(contingency_table[i,:]))
print(row_totals)

# transpose of the matrix:
contingency_table_transpose = contingency_table.transpose()

# exchange for each category (remember that it comes in pairs (Dek):
size_of_exchange_difference = np.array([])
for i in range(0, ncols-1):
    current_exchange_category = np.array([])
    for j in range(0, ncols-1):
        #print(min(contingency_table[i,:][j], contingency_table[:,i][j]))
        current_exchange_category = np.append(current_exchange_category, min(contingency_table[i,:][j], contingency_table[:,i][j]))
        if j == ncols-2:
            size_of_exchange_difference = np.append(size_of_exchange_difference, sum(current_exchange_category)-contingency_table[i,i])
size_of_exchange_difference = size_of_exchange_difference * 2
print(size_of_exchange_difference)

# false alarms for k:
all_false_alarms = np.array([])
for i in range(0, ncols-1):
    all_false_alarms = np.append(all_false_alarms, sum(contingency_table[i,:]) - contingency_table[i,i])
    
# misses for k:
all_misses = np.array([])
for i in range(0, ncols-1):
    all_misses = np.append(all_misses, sum(contingency_table[:,i]) - contingency_table[i,i])


# Quantity difference/disagreement for k (Dqk):
size_of_quantity_difference = abs(all_misses - all_false_alarms)

# size of difference (false alarms + misses) for category k:
size_of_difference = np.array([all_false_alarms + all_misses])

# size of shift difference for k (Dsk):
size_of_shift_difference = size_of_difference - size_of_quantity_difference - size_of_exchange_difference

# sum of quantity, exchange, and shift
qes_sum = size_of_quantity_difference + size_of_exchange_difference + size_of_shift_difference

# false alarm quantity
false_alarm_quantity = np.array([])
for i in range(0, ncols-1):
     false_alarm_quantity = np.append(false_alarm_quantity, max(0, all_false_alarms[i] - all_misses[i]))

# miss quantity
miss_quantity = np.array([])
for i in range(0, ncols-1):
     miss_quantity = np.append(miss_quantity, max(0, all_misses[i] - all_false_alarms[i]))













    