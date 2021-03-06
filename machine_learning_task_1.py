# -*- coding: utf-8 -*-
"""machine learning  task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ViE_PrYhuETOSG5XnzBC0_1oTMByQO4x
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

#preprocessing input data

data = pd.read_csv('/content/MOCK_DATA.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X,Y)
plt.show()

#build the model
m = 0
c = 0

L = 0.0001 #learning rate
epochs = 1000

n = float(len(X))

for i in range(len(X)):
  Y_pred = m*X + c
  D_m = (-2/n) * sum(X * Y - Y_pred)
  D_c = (-2/n) * sum(Y - Y_pred)
  m = m -L*D_m
  c = c- L* D_m
  
print(m,c)

#make prediction
Y_pred = m*X + c
plt.scatter(X,Y)
plt.scatter(X,Y_pred)
plt.show()