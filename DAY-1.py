#DAY-1

import numpy as np

#1.Create an array of integers between -10 and 10

a=np.arange(-10,10)
print(a)

#2. Run the following code to create a NumPy array D

D = np.array(range(18)) + 3

#(a) Extract every other value from array D starting from the 2nd value through the 10th value. Store the result in a variable called x.

X=D[2:10]

#(b) Extract every other value from array D starting from the 10th value through the 2nd value. Store the result in a variable called y.

Y=D[10:2:-1]

#(c) Create a variable z that contains all of the values in D in reverse order.

Z=np.flipud(D))

#3. How are NumPy Arrays better than Lists in Python?

'''
The arrays created with NumPy are more compact than Python Lists.
Accessing arrays and reading and writing elements to arrays is comparatively faster than doing the same in Python Lists.
The arrays created in NumPy are more efficient and convenient to use.
NumPy provides more functionality than the inbuilt Python List.'''

#4. Explain the data types supported by Numpy.
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
