# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:13:30 2024

@author: Triton Perea

Python Data Sciencie Handbook 2nd ed, by VanderPlas
Chapter 5: The basics of Numpy Arrays
"""
import numpy as np
"""-------------
Numpy Array Attributes

"""
# Defining random arrays of one, two and three dimensions

rng = np.random.default_rng(seed=1701)  # seed for random generator

x1 = rng.integers(10, size=6)       # One-dimensional array
x2 = rng.integers(10, size=(3,4))   # Two-dimensional array
x3 = rng.integers(10, size=(3,4,5)) # Three-dimensional array

# We can access at the attributes by:
print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("x3 dtype: ", x3.dtype)

"""----------------
Array indexing: accessing singe elements
"""
# We can access the i_n value (couting form zero) by:
print(x1)
print("Element 0 from x1: ",x1[0])

# To indez from the end of the array, we can use negative indices:
print("Element -1 from x1",x1[-1])

# In a multidimensional array, items can be accessed using a comma-separated
# (row,column) tuple. From x2:
print(x2)
print("Element [0,0] from x2: ",x2[0,0])
print("Element [3,0] from x2: ",x2[3,0])

# Values can also be modified using any of the preceding index notation:
x2[0,0]=12
print(x2)

# If we put a float on a integer space, it will be truncated
x1[0]= 3.14159265 # This will be truncated
print("x1 with new value truncated: ",x1)

"""-------------------
Array Slicing: accessing subarrays
The NumPy slicing syntax follows that of the standard Python list; to access a slice of
an array x, use this:
    
    x[start:stop:step]
"""
# An example of accesing elements in one-D subarrays:
print("Accesing subarrays 1D")
print(x1)
print("First three elements: ", x1[:3])
print("Elements after index 3: ", x1[3:])
print("Middel subarray", x1[1:4])
print("Every second element: ", x1[::2])
print("Every second element, starting at index 1: ", x1[1::2])

