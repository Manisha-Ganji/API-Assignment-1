import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("../Datasets/health_data.csv")
print(df)
# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Checking for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Data type information
print("\nData Types:")
print(df.dtypes)

#Converting data[age]
df['age'] = (df['age'] / 365.25).astype(int)
print(df)
df.to_csv("../Datasets/cardiovascular_dataset.csv")

#View all duplicate rows
duplicates = df.duplicated()
duplicate_rows = df[duplicates]

# Print or inspect duplicate rows
print(duplicate_rows)
#removes the id column from new csv file and saves it.
df = df.drop(df.columns[0], axis=1)
print(df)
df.to_csv("../Datasets/cardiovascular_dataset.csv")





