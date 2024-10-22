import pandas as pd
import numpy as np
 
df = pd.read_csv("../Datasets/cardiovascular_dataset.csv")
#print(df)

# 1. Distance binning
# Formula -> interval = (max-min) / Number of Bins
# Let us consider the 'Age' continuous value column for binning
min_value = df['age'].min()
max_value = df['age'].max()
print("\nMinimum age: " +str(min_value))
print("\nMaximum age: " +str(max_value))

# Suppose the bin size is 5
# linspace returns evenly spaced numbers over a specified interval. 
# Returns num evenly spaced samples, calculated over the interval [start, stop].
bins = np.linspace(min_value,max_value,5)
print("\nSize of bin: 5")
print("\n Display categrories of age based on bin size")
print(bins)

labels = ['Juvenile', 'Adult', 'Middle Age', 'Senior Citizen']

# We can use the cut() function to convert the numeric values of the column Age into the categorical values.
# We need to specify the bins and the labels.
df['bins_dist'] = pd.cut(df['age'], bins=bins, labels=labels, include_lowest=True)
print(df['bins_dist'])
# print(df['bins_dist'].values.tolist())


