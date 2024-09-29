import pandas as pd
from scipy.stats import pearsonr
from matplotlib import pyplot as plt

# Import your data into Python
df = pd.read_csv("../Datasets/cardiovascular_dataset.csv")
 
# Convert dataframe into series
list1 = df['age']
list2 = df['cardio']
 
# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearson correlation: %.3f' % corr)

# Pearson correlation: 0.238 (Moderate Positive correlation)
# Interpretaton:
# As the age of the patient increases,the chance of cardiovascular disease increases
# Scatter plot

# Draw a Plot of the relationship
# 'Age' on the X Axis and 'Cardio' on the Y axis
from matplotlib import pyplot
pyplot.scatter(list1, list2)
pyplot.title('Scatter plot of Age vs Chance of CardioVascular disease')
pyplot.show()
