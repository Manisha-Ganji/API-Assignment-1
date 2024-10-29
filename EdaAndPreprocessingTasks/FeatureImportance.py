# URL Ref - https://machinelearningmastery.com/calculate-feature-importance-with-python/
# For the Covid Dataset, show the feature importance for:
# 1. Decision Tree - CART Feature Importance
# 2. Random Forest
# 3. Permutation Feature Importance - KNN 
import pandas as pd
import numpy as np
 
df = pd.read_csv("../Datasets/cardiovascular_dataset.csv")
print(df)

from sklearn import preprocessing
import matplotlib.pyplot as plt

X = df.iloc[:,[0,1,2,3,4,5,6,7,8,9,10]]   #Age, Gender, Height, Weight, ap_hi(Systolic blood pressure), ap_lo(Diastolic blood pressure), cholrestrol, glucose, smoking, alcohol, pysical activity 
Y = df.iloc[:,[11]]  #cardio disease

# 1. Decision Tree
# Decision tree algorithms like classification and regression trees (CART) offer importance scores based on the reduction in the criterion used to select split points, like Gini or entropy.
# After being fit, the model provides a feature_importances_ property that can be accessed to retrieve the relative importance scores for each input feature.
from sklearn.tree import DecisionTreeClassifier
# define the model
model = DecisionTreeClassifier()
# fit the model
model.fit(X,Y)
# get importance
importance = model.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)
plt.show()

# Results
# Feature: 0, Score: 0.15039
# Feature: 1, Score: 0.02521
# Feature: 2, Score: 0.20573
# Feature: 3, Score: 0.21524
# Feature: 4, Score: 0.24783
# Feature: 5, Score: 0.05569
# Feature: 6, Score: 0.03637
# Feature: 7, Score: 0.02367
# Feature: 8, Score: 0.01164
# Feature: 9, Score: 0.01030
# Feature: 10, Score: 0.01793
# **Indicates that Height, Weight, ap_hi(Systolic blood pressure) are likely candidates for splitting the decision tree.

# 2. Random Forest Feature Importance
# After being fit, the model provides a feature_importances_ property that can be accessed to retrieve the relative importance scores for each input feature.
from sklearn.ensemble import RandomForestRegressor
# define the model
model = RandomForestRegressor()
# fit the model
model.fit(X,Y)
# get importance
importance = model.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)
plt.show()

# Results
# Feature: 0, Score: 0.15377
# Feature: 1, Score: 0.02629
# Feature: 2, Score: 0.19843
# Feature: 3, Score: 0.21333
# Feature: 4, Score: 0.24697
# Feature: 5, Score: 0.05563
# Feature: 6, Score: 0.03917
# Feature: 7, Score: 0.02377
# Feature: 8, Score: 0.01313
# Feature: 9, Score: 0.01026
# Feature: 10, Score: 0.01926
# **Indicates that Height, Weight, ap_hi(Systolic blood pressure) are likely candidates for splitting the decision tree.
# Results are in-tune with the decision tree approach
