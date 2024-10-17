import pandas as pd
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
import io
import base64

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

plt.scatter(list1, list2)
plt.xlabel('Age')
plt.ylabel('Chance of CardioVascular disease')
plt.title('Scatter plot of Age vs Chance of CardioVascular disease')

# Save the plot to a buffer
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Encode the image in base64 and log it
img_base64 = base64.b64encode(buf.read()).decode('utf-8')

# Save the plot as a file
plt.savefig("../output/scatter_plot.png")

# Close the buffer
buf.close()