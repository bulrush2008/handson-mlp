
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

housing_full = pd.read_csv(Path("./datasets/housing/housing.csv"))

print(housing_full.head())
print("-" * 50)

print(housing_full.info())
print("-" * 50)

print(housing_full["ocean_proximity"].value_counts())
print("-" * 50)

print(housing_full.describe())
print("-" * 50)

# the distribution
# extra code – the next 5 lines define the default font sizes
plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

housing_full.hist(bins=50, figsize=(12, 8))

plt.show()