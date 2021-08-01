from pontiPy import *
import pandas as pd

df = pd.read_csv('coastal_1995_2000.csv', index_col= 0)
ob = pontiPy(df)
# _quantity_value = []
# _quantity_label = []
#
# for i in range(len(df.columns)):
#     _quantity = ob.quantity(i, label=True)
#     for key, value in _quantity.items():
#         _quantity_label.append(key)
#         _quantity_value.append(value)
#
# print(_quantity_label)
# print(_quantity_value)


# print("Miss:", ob.miss())
print("Exchange for Category 2:", ob.exchange(1))
print(ob.quantity(2, label=True))
# print("Total Size:", ob.size())
print("Shift:", ob.shift())
# print("Total Difference:", ob.difference())
# print("Difference for Category 2:", ob.difference(2))
#
print("Shift:", ob.shift())
print("Shift:", ob.shift(1))


# #print matrix
# print(ob.matrix())
# print(ob.dataframe)
#
