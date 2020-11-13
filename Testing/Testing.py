from PontiusMatrix import pontiPy
import pandas as pd

df = pd.read_csv('./SampleData/class_sample.csv', index_col= 0)
ob = pontiPy(df)

#
# print("Miss:", ob.miss())
# print("Exchange for Category 2:", ob.exchange(2, Total = True))
# print("Total Size:", ob.size())
# print("Shift:", ob.shift())
# print("Total Difference:", ob.difference())
# print("Difference for Category 2:", ob.difference(2))

print("Shift:", ob.shift())
print("Shift:", ob.shift(1))

#print matrix
print(ob.matrix())
print(ob.dataframe)

