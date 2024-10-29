# Sample Univariate Visualization in Python - Single Column
 
import base64
import io
from pickle import FALSE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


def saveOutput(filename):
    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Encode the image in base64 and log it
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')

    # Save the plot as a file
    plt.savefig("../output/"+filename+".png")

    # Close the buffer
    buf.close()
 
 
# set default theme
sns.set_theme()

# Import your data into Python
df = pd.read_csv("../Datasets/cardiovascular_dataset.csv")
print(df.index)
 
# --------------------------------------- UNIVARIATE ANALYSIS ------------------------------


# 1.1 Box Plot
sns.boxplot(df['age'])   # alternative is plt.boxplot(df['Age'])
plt.title('1. Box Plot of Age')
#plt.show()
saveOutput("univariate01")


#1.2 strip plot is used to visualize the distribution of data points of a single variable
sns.stripplot(y=df['age'])
plt.title('2. Strip Plot of Age')
#plt.show()
saveOutput("univariate02")
 
#1.3 Histograms
plt.hist(df['age'])
plt.title('3. Histogram of Age')
#plt.show()
saveOutput("univariate03")


# 1.4 SNS distplot to plot a histogram
sns.histplot(df['age'], bins=5, kde=True, color='blue')
plt.title('4. Dist Plot of Age with 5 bins')
#plt.show()
saveOutput("univariate04")


# --------------------------------------- BIVARIATE ANALYSIS -----------------------------
 
#2.1 Boxplot - visualize the min, max, median, IQR, outliers of a variable
# 
sns.boxplot(x=df['age'],y=df['ap_hi'],data=df) 
plt.title('5. Box Plot of Age vs Systolic blood pressure')
#plt.show()
saveOutput("bivariate01")



#2.2 Scatter Plot
# Visualize the relationship between two variables
sns.scatterplot(x=df['weight'],y=df['ap_hi'])
plt.title('6. Scatter Plot of Weight vs ap_hi(Systolic blood pressure)')
#plt.show()
saveOutput("bivariate02")


#2.3 FacetGrid 
# Gender vs Discharge Type distribution plot
g = sns.FacetGrid(df, col="gender", height=6.5, aspect=.85)
g.map(sns.histplot, "cardio")
plt.title('7. Facet Grid of Gender vs Cardio Disease')
# plt.show()
saveOutput("bivariate03")
 

#----------------------------- MULTIVARIATE ANALYSIS ----------------------------------
 
# DischargeTypeCategorical vs Age vs Gender distribution plot
g = sns.FacetGrid(df, col="cardio", hue="gender", margin_titles=True, height=6.5, aspect=.85)
g.map(sns.histplot, "age")
plt.title('8. Facet Grid of Gender vs Age vs Cardio Disease')
#plt.show()
saveOutput("multivariate01")
 


# Age vs Gender vs DischargeType
sns.lmplot(data=df, x="age", y="cardio",hue="gender")
plt.title('9. lmplot of Age vs Cardio Disease vs Gender (hue)')
#plt.show()
saveOutput("multivariate02")


# Days of Stay vs Gender vs Age
sns.lmplot(data=df, x="age", y="ap_hi",hue="gender")
plt.title('10. lmplot of Age vs Systolic blood pressure vs Gender (hue)')
#plt.show()
saveOutput("multivariate03")
 

# Days of Stay vs DischargeTypeCategorical vs Age
sns.lmplot(data=df, x="age", y="ap_hi",hue="cardio")
plt.title('11. lmplot of age vs Systolic blood pressure vs Cardio Disease(hue)')
saveOutput("multivariate04")
#plt.show()


