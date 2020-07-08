# Coursera Python for Data Science and AI, IBM
## Week 4
import pandas as pd
import math
import numpy as np

#Making Data Frames
prac = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

claremont = {"College":['Pomona', 'Pitzer', 'Scripps','CMC', 'HMC'],
'Founded':[1887, 1963, 1921, 1942, 1957],
 'Size': [1700, 1100, 1000, 1300, 900]
 }

colleges = pd.DataFrame(claremont)
years = colleges[["Founded", "Size"]]

##Locate using row and column indices
### loc is largely label based
colleges.loc[0, "Size"]
### iloc is integer-based
colleges.iloc[2,2]
### ix looks for a label by default but uses an
### integer if it can't find one

#Pandas: Working with and Saving Data
unique_cols = colleges['Founded'].unique()

newest = colleges[colleges["Founded"] >= 1930]


#Create new CSV
#colleges.to_csv('claremont_colleges.csv')

##One Dimensional Numpy
a = np.array([0,1,2,3,4]) # <- type np/numpy.array
a.size
a.ndim
a.shape

a[0] = 47
a[-1] = 69

b = a[0:]


### Basic Operations
u = np.array([2,3])
v = np.array([4,5])

u + v
u - v
2 * u # Scalar multiplication
u * v # Vector multiplication
np.dot(u, v) # Dot product

mean_u = u.mean # Mean of array values
max_u = u.max() # Maximum array value

pi = np.pi
w = np.array( [0, pi/2, (3*pi)/2, 2*pi] ) # Unit circle
z = np.sin(w) # Applies sine fcn to each component

np.linspace(-2, 2, num = 9) # Gives num evenly spaced integers in the range

x = np.linspace(0, 2*pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.show()

plt.plot(x, y)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.plot([1,2, 3, 4], [1, 2, 3, 4])

## 2D Numpy
aa = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

AA = np. array(aa)
AA.ndim # Think of the number of nested lists
AA.shape # Number of nested lists (rows), size of each list (cols)
AA.size # Total number of elements

import numpy as np
from matplotlib import pyplot
