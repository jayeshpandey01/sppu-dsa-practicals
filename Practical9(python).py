'''
This program is created by ATHARVA PAWAR

Experiment No. 9 : Write a Python Program to compute following computation on matrices :
                   a)Addition of two matrices
                   b)Subtraction of two matrices
                   c)Multiplication of two matrices
                   d)Transpose of a matix
'''
import numpy

# Initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

# Using add() to add matrices
print("The element-wise addition of matrices is:")
print(numpy.add(x, y))

# Using subtract() to subtract matrices
print("The element-wise subtraction of matrices is:")
print(numpy.subtract(x, y))

# Using dot() to multiply matrices
print("The matrix multiplication (dot product) result is:")
print(numpy.dot(x, y))

# Using "T" to transpose the matrix
print("The transpose of the given matrix x is:")
print(x.T)
