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
contingency_table_np = np.loadtxt(open(my_path, "rb"), 
                               delimiter = ",", 
                               skiprows = 1,
                               usecols = range(1, ncols))
print(contingency_table_np)


#find sum of hits:
total_hits_np = 0
for i in range(0, ncols-1):
    total_hits_np = total_hits_np + contingency_table_np[i,i]
    
#find column sums
column_totals_np = np.array([])
for i in range(0, ncols-1):
    column_totals_np = np.append(column_totals_np, sum(contingency_table_np[:,i]))

# find row totals:
row_totals_np = np.array([])
for i in range(0, ncols-1):
    row_totals_np = np.append(row_totals_np, sum(contingency_table_np[i,:]))


# transpose of the matrix:
contingency_table_transpose_np = contingency_table_np.transpose()

# exchange for each category (remember that it comes in pairs (Dek):
size_of_exchange_difference_np = np.zeros(shape=(1, ncols-1))
for i in range(0, ncols-1):
    current_exchange_category = np.zeros(shape=(1, ncols-1))
    for j in range(0, ncols-1):
        current_exchange_category[0,j] = np.min((contingency_table_np[i,:][j], contingency_table_np[:,i][j]))
        if j == ncols-2:
            size_of_exchange_difference_np[0,i] = np.sum(current_exchange_category)-contingency_table_np[i,i]
size_of_exchange_difference_np = size_of_exchange_difference_np * 2


# false alarms for k:
all_false_alarms_np = np.zeros(shape=(1, ncols-1))
for i in range(0, ncols-1):
    all_false_alarms_np[0,i] =  sum(contingency_table_np[i,:]) - contingency_table_np[i,i]
    
# misses for k:
all_misses_np = np.zeros(shape=(1, ncols-1))
for i in range(0, ncols-1):
    all_misses_np[0,i] = sum(contingency_table_np[:,i]) - contingency_table_np[i,i]


# Quantity difference/disagreement for k (Dqk):
size_of_quantity_difference_np = abs(all_misses_np - all_false_alarms_np)

# size of difference (false alarms + misses) for category k:
size_of_difference_np = all_false_alarms_np + all_misses_np

# size of shift difference for k (Dsk):
size_of_shift_difference_np = size_of_difference_np - size_of_quantity_difference_np - size_of_exchange_difference_np

# sum of quantity, exchange, and shift
qes_sum_np = size_of_quantity_difference_np + size_of_exchange_difference_np + size_of_shift_difference_np

# false alarm quantity
false_alarm_quantity_np = np.zeros(shape = (1, ncols-1))
for i in range(0, ncols-1):
    false_alarm_quantity_np[0,i] = np.max((0, (all_false_alarms_np[0,i] - all_misses_np[0, i])))

# miss quantity
miss_quantity_np = np.zeros(shape = (1, ncols-1))
for i in range(0, ncols-1):
    miss_quantity_np[0,i] = np.max((0, (all_misses_np[0,i] - all_false_alarms_np[0, i])))



#create Size dataframe:
categories_np = np.array([range(0, ncols-1)])










    