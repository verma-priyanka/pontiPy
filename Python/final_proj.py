# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:40:21 2019

@author: JFrey
"""

import numpy as np
# import pandas as pd

#file path:
# E:/OneDrive/Documents/School_Work/Clark/Map_Comparison/final_proj/PontiusMatrix/Data/contingency.csv
# D:/OneDrive/Documents/School_Work/Clark/Map_Comparison/final_proj/PontiusMatrix/Data/contingency.csv

#specify whether 



my_path = input("Enter the file path: ")

# find the number of columns in csv
with open(my_path) as f:
    ncols = len(f.readline().split(',')) #comma delimited

# load in csv, skipping first row and column
contingency_table_np = np.loadtxt(open(my_path, "rb"), 
                               delimiter = ",", 
                               skiprows = 1,
                               usecols = range(1, ncols))

#contingency_table_pd = pd.read_csv(my_path, 
#                                   sep=',',
#                                   header='infer', #specify header (automatically detect)
#                                   index_col = 0) #specify rownames

#find sum of hits:
def sum_of_hits(data):
    total_hits_np = 0
    for i in range(0, len(data)):
        total_hits_np = total_hits_np + data[i,i]
    return total_hits_np

#def sum_of_hits(data):
#    total_hits_pd = 0
#    for i in range(0, len(data)):
#        total_hits_pd = total_hits_pd + data.iloc[i,i]
#    return(total_hits_pd)
    
#find column sums
def column_totals(data):
    column_totals_np = np.zeros(shape=(1, len(data)))
    for i in range(0, len(data)):
        column_totals_np[0,i] = np.sum((data[:,i]))
    return(column_totals_np)

#def column_totals(data):
#    column_totals_pd = contingency_table_pd.sum(axis=0)
#    return(column_totals_pd)


# find row totals:
def row_totals(data):
    row_totals_np = np.zeros(shape=(1, len(data)))
    for i in range(0, len(data)):
        row_totals_np = np.sum((data[i,:]))
    return(row_totals_np)

#def row_totals(data):
#    row_totals_pd = contingency_table_pd.sum(axis=1)
#    return(row_totals_pd)

# transpose of the matrix:
def transpose(data):
    contingency_table_transpose_np = data.transpose()
    return(contingency_table_transpose_np)

#def transpose(data):
#    contingency_table_transpose_pd = data.transpose()
#    return(contingency_table_transpose_pd)


# exchange for each category (remember that it comes in pairs (Dek):
def size_of_exchange_difference(data):
    size_of_exchange_difference_np = np.zeros(shape=(1, len(data)))
    for i in range(0, len(data)):
        current_exchange_category = np.zeros(shape=(1, len(data)))
        for j in range(0, len(data)):
            current_exchange_category[0,j] = np.min((data[i,:][j], data[:,i][j]))
            if j == len(data)-1:
                size_of_exchange_difference_np[0,i] = np.sum(current_exchange_category)-data[i,i]
    size_of_exchange_difference_np = size_of_exchange_difference_np * 2
    return(size_of_exchange_difference_np)


#def size_of_exchange_difference(data):
#    blah = []
#    for i in range(0, len(data)):
#        current_category = []
#        for j in range(0, len(data)):
#            current_category.append(min(data.iloc[i,j], data.iloc[j,i]))
#            if j == len(data)-1:
#                blah.append(sum(current_category) - data.iloc[i,i])
#    return([n*2 for n in blah])
                

# false alarms for k:
def false_alarms(data):
    all_false_alarms_np = np.zeros(shape=(1, len(data)))
    for i in range(0, len(data)):
        all_false_alarms_np[0,i] =  sum(data[i,:]) - data[i,i]
    return(all_false_alarms_np)
    
#def false_alarms(data):
#    false_alarms_pd = []
#    for i in range(0, len(data)):
#        false_alarms_pd.append(data.iloc[i,:].sum(axis=0)-data.iloc[i,i])
#    return(false_alarms_pd)

# misses for k:
def misses(data):
    all_misses_np = np.zeros(shape=(1, len(data)))
    for i in range(0, len(data)):
        all_misses_np[0,i] = sum(data[:,i]) - data[i,i]
    return(all_misses_np)

#def misses(data):
#    all_misses_pd = []
#    for i in range(0, len(data)):
#        all_misses_pd.append(data.iloc[:,i].sum(axis=0) - data.iloc[i,i])
#    return(all_misses_pd)


# Quantity difference/disagreement for k (Dqk):
def size_of_quantity_difference(data):
    size_of_quantity_difference_np = abs(misses(data) - false_alarms(data))
    return(size_of_quantity_difference_np)

# size of difference (false alarms + misses) for category k (total disagreement):
def size_of_difference(data):
    size_of_difference_np = false_alarms(data) + misses(data)
    return(size_of_difference_np)

# size of shift difference for k (Dsk):
def size_of_shift_difference(data):
    size_of_shift_difference_np = size_of_difference(data) - size_of_quantity_difference(data) - size_of_exchange_difference(data)
    return(size_of_shift_difference_np)
    
# sum of quantity, exchange, and shift
def qes(data):
    qes_sum_np = size_of_quantity_difference(data) + size_of_exchange_difference(data) + size_of_shift_difference(data)
    return(qes_sum_np)
    
# false alarm quantity
def false_alarm_quantity(data):
    false_alarm_quantity_np = np.zeros(shape = (1, len(data)))
    for i in range(0, len(data)):
        false_alarm_quantity_np[0,i] = np.max((0, (false_alarms(data)[0,i] - misses(data)[0,i])))
    return(false_alarm_quantity_np)
    
# miss quantity
def miss_quantity(data):
    miss_quantity_np = np.zeros(shape = (1, len(data)))
    for i in range(0, len(data)):
        miss_quantity_np[0,i] = np.max((0, (misses(data)[0,i] - false_alarms(data)[0, i])))
    return(miss_quantity_np)


# miss exchange

# false alarm exchange


# extent of contingency table (total pixel count)
def extent(data):
    return(np.sum(data))


# allocation disagreement
#def allocation_disagreement(data):
#    return((sum_of_misses(data) - sum_of_false_alarms(data)) - abs(sum_of_misses(data) - sum_of_false_alarms(data)))

# sum of correct rejections
def correct_rejections(data):
    if len(data) > 2:
        print("You may only have 2 categories (presence and absence) for this metric.")
    else:
        return(extent(data) - data[0,0] - data[0,1] - data[1,0])

       
# sensitivity
def sensitivity(data):
    if len(data) == 2:
        return(data[0,0] / (data[0,0] + data[1,0]))
    else:
        print("You may only have 2 categories (presence and absence) for this metric.")

# specificity:
def specificity(data):
    if len(data) > 2:
        print("You may only have 2 categories (presence and absence) for this metric.")
    else:
        correct_rejections(data) / (correct_rejections(data) + data[1,0])


def sample_to_population(data, transformation = 1):
    if np.shape(transformation) == (len(data), 1) or type(transformation) == int:
        return(data * transformation)
    else:
        print("The tranformation array provided has incorrect dimensions.")


