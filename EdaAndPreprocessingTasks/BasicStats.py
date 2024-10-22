import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("../Datasets/health_data.csv")
print("\nDisplaying the original daatset after loading into dataframe:\n")
print(df)
# Summary statistics
print("\nSummary Statistics:\n")
print(df.describe(include='all'))

# Checking for missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Data type information
print("\nData Types:\n")
print(df.dtypes)

# Converting data[age]
print("\nConverting age from number days to number of years\n")
df['age'] = (df['age'] / 365.25).astype(int)
print(df)
df.to_csv("../Datasets/cardiovascular_dataset.csv")

# View all duplicate rows
duplicates = df.duplicated()
duplicate_rows = df[duplicates]

# Print or inspect duplicate rows
print("\nDuplicate rows\n")
print(duplicate_rows)
# removes the id column from new csv file and saves it.
print("\nRemoving patient id column\n")
df = df.drop(df.columns[0], axis=1)
print(df)
df.to_csv("../Datasets/cardiovascular_dataset.csv")





