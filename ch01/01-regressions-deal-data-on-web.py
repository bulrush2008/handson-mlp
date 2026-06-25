
from statistics import mode

from packaging.version import Version
import sklearn
import sys

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# this project requires Python 3.10 or above
assert sys.version_info >= (3, 10), "This script requires Python 3.10 or higher."

# It also requires Scikit-Learn >= 1.6.1
assert Version(sklearn.__version__) >= Version("1.6.1")

# let's define the default font sizes, to plot pretty figures
plt.rc('font',size=12)
plt.rc('axes',labelsize=14,titlesize=14)
plt.rc('legend', fontsize=12)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)

# code exammple 1-1

# 直接从网络读取数据：缓存，但并不下载存储到本地
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Visualize the data
lifesat.plot(kind="scatter", x="GDP per capita (USD)", y="Life satisfaction", grid=True)
plt.axis([23_500, 62_500, 4, 9])
plt.savefig("lifesat_scatterplot.png")

# Select a linear model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make a prediction for Puerto Rico
X_new = [[33_442.8]]  # Puerto Rico's GDP per capita in 2020
print("Prediction with Linear Regression: ", model.predict(X_new))  # outputs approximate [[6.02]]

# change to use KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)
print("Prediction with KNN: ", model.predict(X_new))  # outputs approximate [[5.73]]