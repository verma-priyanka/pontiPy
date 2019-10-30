# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:40:21 2019

@author: JFrey
"""

import numpy as np
import pandas as pd

#file path:
# E:/OneDrive/Documents/School_Work/Clark/Map_Comparison/final_proj/PontiusMatrix/Data/contingency.csv
# D:/OneDrive/Documents/School_Work/Clark/Map_Comparison/final_proj/PontiusMatrix/Data/contingency.csv

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

    
#find column sums
column_totals = np.array([])
for i in range(0, ncols-1):
    column_totals = np.append(column_totals, sum(contingency_table[:,i]))

# find row totals:
row_totals = np.array([])
for i in range(0, ncols-1):
    row_totals = np.append(row_totals, sum(contingency_table[i,:]))


# transpose of the matrix:
contingency_table_transpose = contingency_table.transpose()

# exchange for each category (remember that it comes in pairs (Dek):
size_of_exchange_difference = np.zeros(shape=(1, ncols-1))
for i in range(0, ncols-1):
    current_exchange_category = np.zeros(shape=(1, ncols-1))
    for j in range(0, ncols-1):
        current_exchange_category[0,j] = np.min((contingency_table[i,:][j], contingency_table[:,i][j]))
        if j == ncols-2:
            size_of_exchange_difference[0,i] = np.sum(current_exchange_category)-contingency_table[i,i]
size_of_exchange_difference = size_of_exchange_difference * 2


# false alarms for k:
all_false_alarms = np.zeros(shape=(1, ncols-1))
for i in range(0, ncols-1):
    all_false_alarms[0,i] =  sum(contingency_table[i,:]) - contingency_table[i,i]
    
# misses for k:
all_misses = np.zeros(shape=(1, ncols-1))
for i in range(0, ncols-1):
    all_misses[0,i] = sum(contingency_table[:,i]) - contingency_table[i,i]


# Quantity difference/disagreement for k (Dqk):
size_of_quantity_difference = abs(all_misses - all_false_alarms)

# size of difference (false alarms + misses) for category k:
size_of_difference = all_false_alarms + all_misses

# size of shift difference for k (Dsk):
size_of_shift_difference = size_of_difference - size_of_quantity_difference - size_of_exchange_difference

# sum of quantity, exchange, and shift
qes_sum = size_of_quantity_difference + size_of_exchange_difference + size_of_shift_difference

# false alarm quantity
false_alarm_quantity = np.zeros(shape = (1, ncols-1))
for i in range(0, ncols-1):
    false_alarm_quantity[0,i] = np.max((0, (all_false_alarms[0,i] - all_misses[0, i])))

# miss quantity
miss_quantity = np.zeros(shape = (1, ncols-1))
for i in range(0, ncols-1):
    miss_quantity[0,i] = np.max((0, (all_misses[0,i] - all_false_alarms[0, i])))



#create Size dataframe:
categories = np.array([range(0, ncols-1)])









    