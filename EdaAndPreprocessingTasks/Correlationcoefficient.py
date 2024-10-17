
from tkinter import TRUE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

 
df = pd.read_csv("../Datasets/cardiovascular_dataset.csv")

df = df.drop(df.columns[0], axis=1)
df.to_csv("../Datasets/cardiovascular_dataset.csv", index=False)
print(df)

# Correlation Matrix - Internally uses Pearson Correlation
cor = df.corr()

# Plotting Heatmap
plt.figure(figsize = (12,6))
sns.heatmap(cor, annot=True)


# Save the heatmap to a buffer
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Encode the image in base64 and log it
img_base64 = base64.b64encode(buf.read()).decode('utf-8')

# Save the heatmap as a file
plt.savefig("../output/heat_map.png")

# Close the buffer
buf.close()
