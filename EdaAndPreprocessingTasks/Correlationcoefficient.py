from tkinter import TRUE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("../Datasets/cardiovascular_dataset.csv")

df = df.drop(df.columns[0], axis=1)
df.to_csv("../Datasets/cardiovascular_dataset.csv", index=False)
print(df)

# Correlation Matrix - Internally uses Pearson Correlation
cor = df.corr()

# Plotting Heatmap
plt.figure(figsize = (12,6))
sns.heatmap(cor, annot=True)
plt.show()
