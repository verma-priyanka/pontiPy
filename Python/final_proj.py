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


my_path = input("Enter the file path: ")

# find the number of columns in csv
with open(my_path) as f:
    ncols = len(f.readline().split(',')) #comma delimited

# load in csv, skipping first row and column
contingency_table_np = np.loadtxt(open(my_path, "rb"), 
                               delimiter = ",", 
                               skiprows = 1,
                               usecols = range(1, ncols))



#find sum of hits:
#def sum_of_hits(data):
#    total_hits_np = 0
#    for i in range(0, len(data)):
#        total_hits_np = total_hits_np + data[i,i]
#    return total_hits_np

# extent of contingency table (total pixel count)
def extent(data):
    return(np.sum(data))

# misses (binary or k):
def misses(data, par1='ALL'):
    if len(data) > 2:
        all_misses_np = np.zeros(shape=(1, len(data)))
        for i in range(0, len(data)):
            all_misses_np[0,i] = sum(data[:,i]) - data[i,i]
        if par1 == 'ALL':
            return(all_misses_np)
        else:
            return(all_misses_np)[0, par1]
    else:
        return(data[1,0])

# hits (binary or k):
def hits(data, par1='ALL'):
    if len(data) > 2:
        all_hits_np = np.zeros(shape=(1, len(data)))
        for i in range(0, len(data)):
            all_hits_np[0,i] = data[i,i]
        if par1 == 'ALL':
            return(all_hits_np)
        else:
            return(all_hits_np[0, par1])
    else:
        return(data[0,0])
        

#correct rejections
def correct_rejections(data):
    if len(data) > 2:
        print("You may only have 2 categories (presence and absence) for this metric.")
    else:
        return(data[1,1])
        
# false alarms for k:
def false_alarms(data, par1='ALL'):
    if len(data) > 2:
        all_false_alarms_np = np.zeros(shape=(1, len(data)))
        for i in range(0, len(data)):
            all_false_alarms_np[0,i] =  sum(data[i,:]) - data[i,i]
        if par1 == 'ALL':
            return(all_false_alarms_np)
        else:
            return(all_false_alarms_np[0, par1])
    else:
        return(data[0,1])
    
# sensitivity
def sensitivity(data):
    if len(data) == 2:
        return(hits(data) / (hits(data) + misses(data)))
    else:
        print("You may only have 2 categories (presence and absence) for this metric.")

# specificity:
def specificity(data):
    if len(data) > 2:
        print("You may only have 2 categories (presence and absence) for this metric.")
    else:
        correct_rejections(data) / (correct_rejections(data) + false_alarms(data))

# convert sample to population
def sample_to_population(data, transformation = 1):
    if (type(transformation) == np.ndarray and np.shape(transformation) == (len(data), 1)) or type(transformation) == int:
        return(data * transformation)
    elif type(transformation) == list:
        transformation = np.vstack(np.array(transformation))
        return(data * transformation)
    else:
        print("The tranformation array provided has incorrect dimensions.")
    
#find column sums
def column_totals(data):
    column_totals_np = np.zeros(shape=(1, len(data)))
    for i in range(0, len(data)):
        column_totals_np[0,i] = np.sum((data[:,i]))
    return(column_totals_np)


# find row totals:
def row_totals(data):
    row_totals_np = np.zeros(shape=(1, len(data)))
    for i in range(0, len(data)):
        row_totals_np = np.sum((data[i,:]))
    return(row_totals_np)



# transpose of the matrix:
def transpose(data):
    contingency_table_transpose_np = data.transpose()
    return(contingency_table_transpose_np)


# total exchange for each category (remember that it comes in pairs (Dek):
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

    

# Quantity difference/disagreement for k (Dqk):
def size_of_quantity_difference(data):
    size_of_quantity_difference_np = abs(misses(data) - false_alarms(data))
    return(size_of_quantity_difference_np)

#######################
#def is_quantity(data, par1=None):
#    bool_list = np.ndarray.tolist(size_of_quantity_difference(data) > 0)[0]
#    return([i for i, x in enumerate(bool_list) if x])[par1]

# size of difference (false alarms + misses) for category k (total disagreement):
def size_of_difference(data):
    size_of_difference_np = false_alarms(data) + misses(data)
    return(size_of_difference_np)

# size of shift difference for k (Dsk), (shift):
def size_of_shift_difference(data):
    if len(data > 2):
        size_of_shift_difference_np = size_of_difference(data) - size_of_quantity_difference(data) - size_of_exchange_difference(data)
        return(size_of_shift_difference_np)
    else:
        print("You must have more than presence and absence categories for this metric.")
    
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

# total quantity
def quantity(data):
    total_quantity = np.zeros(shape = (1, len(data)))
    for i in range(0,len(data)):
        if miss_quantity(data)[0,i] != false_alarm_quantity(data)[0,i]:
            total_quantity[0,i] = max(miss_quantity(data)[0,i], false_alarm_quantity(data)[0,i])
        else:
            total_quantity[0,i] = 0
    return(total_quantity)
    

## miss exchange
#def miss_exchange(data, par1 = 'ALL', par2 = 'ALL'):
#    exchange = np.zeros(shape=(1, len(data)))
#    if par1 == "ALL":
#        for i in range(0, len(data)):
#            current_exchange_category = np.zeros(shape=(1, len(data)))
#            for j in range(0, len(data)):
#                current_exchange_category[0,j] = np.min((data[i,:][j], data[:,i][j]))
#                if j == len(data)-1:
#                    exchange[0,i] = np.sum(current_exchange_category)-data[i,i]
#        return(exchange)
#    elif type(par1) == int:
#        current_exchange_category = np.zeros(shape=(1, len(data)))
#        for j in range(0, len(data)):
#            if j == len(data)-1:
#                current_exchange_category[0,j] = np.min((data[par1,:][j], data[:,par1][j]))
##    
def convert_to_pandas(my_array):
    x = pd.DataFrame(data = np.int_(my_array[0:, 0:]),
                 index = range(0, len(my_array)),
                 columns = range(0, len(my_array)))
    return(x)
        

##df_transpose = df.transpose()
#def exchange(my_np_array, category1 = 'ALL',category2 = 'ALL'):
#    dataframe = convert_to_pandas(my_np_array)
#    _exchange = {}
#    _categories = range(len(dataframe)-1)
#    for i in _categories:
#        # Create a list for every category
#        _catlist = []
#        for j in _categories:
#            if i != j:
#                # Create list with each exchange value for category 1
#                _catlist.append(min(dataframe.transpose().iloc[i][j],dataframe.transpose().iloc[j][i]))
#        # Append exchange list for each category to dictionary
#        _exchange[i]=_catlist
#        # print('Exchange for Category',i,": ",_catlist)
#    # A condensed list of category and exchange sum for each
#    ex_by_category = ({k: sum(v) for k, v in _exchange.items()})
#    if category1 == 'ALL':
#        # Total exchange. Should this be divided by 2?
#        return sum(ex_by_category.values())
#    # If one category is specified
#    # Return is exchange with all categories
#    elif category1 != 'ALL' and category2 == 'ALL':
#        # Dictionary to return exchanges between cat 1 and all other categories
#        # Also returns a total exchange for category
#        _single_category= {}
#        # iterate through number of categories
#        for i in range(len(_exchange[category1])):
#            # Exchange at index 0 = exchange of 0 with category 1 since exchange cannot happen with itself
#            # Size of list with exchange is # of categories - 1
#            # If index of list item == category 1, the exchange is for the category after
#            # Example: Parameter is Category 2
#            # Exchange for Category 2: {'Category 0': 0, 'Category 1': 30, 'Category 3': 40, 'Total Exchange': 70}
#            if i != category1:
#                # key for dictionary
#                _cat_key = 'Category ' + str(i)
#                # If i == category, the else statement added that category to dict
#                # So this addition will be i+1
#                if _cat_key in _single_category.keys():
#                    _cat_key = 'Category ' + str(i + 1)
#                    _single_category[_cat_key] = _exchange[category1][i]
#                # if category i not in dictionary, add to dictionary
#                else:
#                    _single_category[_cat_key] = _exchange[category1][i]
#            # Exchange at index 0 = exchange of 0 with category 1
#            # When index == category1 parameter, the key will be incremented by 1
#            # Category 1 Exchange with Category 0 = index 0 in list
#            else:
#                _cat_key = 'Category ' + str(i+1)
#                _single_category[_cat_key] = _exchange[category1][i]
#        _single_category['Total Exchange'] = sum(_single_category.values())
#        return _single_category
#    else:
#        # Exchange is with the inverse cell position for the two categories
#        return min(_exchange[category1][category2],_exchange[category2][category1])

#print("Exchange for Category 2:",exchange(dataframe.transpose().index,2))



# ------------------------------------------------------------------------------
# This function will call all the previous functions
# This will generate the final output contingency table Prissskilla designs
def contingency_table(dataframe):
    dataframe.loc["False Alarm"] = false_alarm(dataframe.index)
    return dataframe


# miss shift
    
# false alarm shift
        


# allocation disagreement
#def allocation_disagreement(data):
#    return((sum_of_misses(data) - sum_of_false_alarms(data)) - abs(sum_of_misses(data) - sum_of_false_alarms(data)))








import rasterio
import rasterio.plot
import pyproj
import matplotlib
import matplotlib.pyplot as plt
x = "D:/OneDrive/Documents/School_Work/Clark/Map_Comparison/hw1/map_comparison_hw1/1971Landcover01_bool.rst"
y = "D:/OneDrive/Documents/School_Work/Clark/Map_Comparison/hw1/map_comparison_hw1/1985Landcover01_bool.rst"
#print file metadata
with rasterio.open(x) as src1:
    print(src1.profile)

#access and plot values as numpy array
with rasterio.open(x) as src1:
     my_raster_array1 = src1.read(1, out_shape=(1, int(src1.height), int(src1.width)))
     print(my_raster_array1)
plt.imshow(my_raster_array1)
plt.colorbar()
plt.title("1971")
plt.xlabel("Column #")
plt.ylabel("Row #")
         
           
with rasterio.open(y) as src2:
    print(src2.profile)

#access and plot values as numpy array
with rasterio.open(y) as src2:
     my_raster_array2 = src2.read(1, out_shape=(1, int(src2.height), int(src2.width)))
     print(my_raster_array2)
plt.imshow(my_raster_array2)
plt.colorbar()
plt.title("1985")
plt.xlabel("Column #")
plt.ylabel("Row #")
         
from sklearn.metrics import confusion_matrix
my_raster_vec1 = np.reshape(my_raster_array1, my_raster_array1.size)
my_raster_vec2 = np.reshape(my_raster_array2, my_raster_array2.size)

confusion_matrix(my_raster_vec1, my_raster_vec2)




