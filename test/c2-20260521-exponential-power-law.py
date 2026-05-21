
# compare two distributions: exponential and power law

import numpy as np
import matplotlib.pyplot as plt

# generate data
x = np.linspace(1, 1000, 5000)
y_exp = np.exp(-x / 20)  # exponential distribution
y_power = x ** (-5)  # power law distribution

# plot the distributions
plt.figure(figsize=(10, 6))
plt.plot(x, y_exp, label='Exponential Distribution', color='blue')
plt.plot(x, y_power, label='Power Law Distribution', color='orange')
#plt.xscale('log')
plt.yscale('log')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Exponential and Power Law Distributions')

plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('exponential_power_law_comparison.png')  # save the figure
#plt.show()