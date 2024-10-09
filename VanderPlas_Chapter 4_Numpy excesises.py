# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:37:06 2024

@author: Triton Perea

Python Data Sciencie Handbook 2nd ed, by VanderPlas
Chapter 4
"""

""" ------------
A Python List Is More Than Just a List
The standard mutable multielement container in Python is the list.
"""
# We can create a list of integers as follows:
L = list(range(10))
print(L)            # We can print the entire list
print(type(L[0]))          # We can know the type of each object in the list, since the terminal

# Or, similarly, a list of string:
L2 = [str(c) for c in L]        # str(x) convert the number x in string. This is for every element on the list L
print(L2)
print(type(L2[0]))

# Because of Python’s dynamic typing, we can even create heterogeneous lists
L3 = [True, "2", 3.0, 4]
print(L3)
print([type(item)for item in L3])

"""----------------
Fixed-type Arrays in Python
The built-in array module (available since Python 3.3) can be used to create
dense arrays of a uniform type.
"""
import array
L = list(range(10))
A = array.array('i', L) # Here, we create an fixed-type array (of integers) from list L
print(A)                # Here,'i' is a type code indicating the contents are integers.

"""----------------
Creating Arrays from Python lists
Here, we start using the Numpy package
"""
import numpy as np

#Now we can use np.array to create arrays from Python lists
arr = np.array([1,4,2,5,3])
print(arr)
# NumPy arrays can only contain data of the same type
# If the types do not match, NumPy will upcast them according to its type promotion rules
arr2 = np.array([3.14, 4, 2, 3])
print(arr2)

# If we want to explicitly set the data type of the array, we can use 'dtype':
arr3 = np.array([2,1,3,4], dtype=np.float32)
print("Array dtype float 32", arr3)

# Unlike Python lists, which are always one-dimensional sequences, NumPy arrays can be multidimensional.
arrMulti = np.array([range(i, i+4) for i in [2, 4, 6]])
print("Array multidimensional",arrMulti)

"""-------------------
Creating arrays from Scratch
Especially for larger arrays, it is more efficient to create arrays from scratch using routines
built into NumPy
"""
# Create a length-10 integer array filled with 0s
arrZeros = np.zeros(10, dtype=int)  #dtype= int --> integers
print("Array length-10 zeros",arrZeros)

# Create a 3x5 floating-point array filled with 1s
arrOnes= np.ones((3,5), dtype=float)    # (3,5) := 3x5 
print("Array 3x5 1s dtype float", arrOnes)

# Create a 3x5 array filled with 3.14
arrPi = np.full((3,5), 3.14)        # 3.14 indicates anything you want in all (full) places of the array
print("Array 3x5 with 3.14", arrPi)

# Create an array filled with a linear sequence starting at 0
# ending at 20, stepping by 2 (this is similar to the built-in range function)
arrLinear = np.arange(0, 20, 2)
print("Array with linear sequence", arrLinear)

# Create an array of five values evenly spaced between 0 and 1
arrLins = np. linspace(0, 1, 5)  #Start at 0, finish in 1, with 5 numbers
print("Array that start at 0, finish in 1, with 5 numbers ", arrLins)

# Create a 3x3 array of uniformly distributed pseudorandom values between 0 and 1
arrRandom = np.random.random((3,3))
print("Array random between 0 and 1", arrRandom)

# Create a 3x3 array of normally distributed pseudorandom values with mean 0 and standard deviation 1
arrRNormal = np.random.normal(0,1,(3,3))
print("Array random 2", arrRNormal)

# Create a 3x3 array of pseudorandom integers in the interval [0,10]
arrRInt = np.random.randint(0,10,(3,3))
print("Array of int [0,10], random", arrRInt)

# Create a 3x3 identity matrix
arrIdentity = np.eye(3)
print("3x3 identity matrix", arrIdentity)

# Create an uninitialized array of three integers
arrEmpty = np.empty(3)
print("3x3 array empty", arrEmpty)
