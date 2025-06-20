# -*- coding: utf-8 -*-
"""kmeans_mall.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WR1tZ9OhiorTxZ9h--YGEcb0Q65kSgOG
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

cus.head()

cus=pd.read_csv("/content/Mall_Customers.csv")

cus.isnull().sum()

cus.shape

"""**to select the paticular column**"""

X=cus.iloc[:,[3,4]].values

print(X)

cus.info()

"""**finding wcss value for each data**"""

wcss = []

for i in range(1,11):
  Kmeans = KMeans(n_clusters = i, init = 'k-means++',random_state=42)
  Kmeans.fit(X)

  wcss.append(Kmeans.inertia_)

k=KMeans(n_clusters=5,init='k-means++',random_state=0)
y=k.fit_predict(X)
print(y)

sns.set()
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()