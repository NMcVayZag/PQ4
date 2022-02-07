import numpy as np 

x = list(range(10))
print(x)

#make a numpy ndarray
x = np.array(x)
print(x)
print(type(x))

# 2D
x = [[1,2,3],[4,5,6]]
print(x)
x = np.array(x)
print(x)
print(x.ndim)
print(x.shape) #rows x collumns 
print(x.dtype)
# convert x to be an array of floats 
x_floats = x.astype(np.float)
print(x_floats)
print(x_floats.dtype) #numpys float designation

x = np.arange(2,10,.5) #start, stop, step
print(x)

x = np.ones((4,5))
print(x)

x = np.zeros((4,5))
print(x)

x = np.full(10, 5.5)
print(x)

#indexing
x = np.ones((4,5))
print(x[0][0], x[0, 0])   #these print indexing are equivalent

#vectorization #IMPORTANT
#applying an operation to all elements in a array without using a loop
x = list(range(10))
y = list(range(10,20))
print(x)
print(y)
z = []
for i in range(len(x)):
    z.append(x[i] + y[i])
print(z)
#without loops - Vectorization

x = np.arange(10)
y = np.arange(10,20)
print(x)
print(y)
z = x + y #wala
print(z)

#relational operators are also vectorized with numpy
m_names = np.array(["Mary", "Michael", "Margaret", "Mary", "Marcus", "Molly"])
m_ages = np.array([   28,      72,         12,         34,      40,       68])
#boolean array
marys = m_names == "Mary"
print(marys)
# we can do boolean indexing with a boolean array
mary_ages = m_ages[marys] #only index into m_ages where m_names are mary
print(mary_ages)

# and, or, not are vectorized as &, |, ~(boolean arrays) or np.logical_not() (for integer arrays)

# broadcasting = operations between different sized arrays 
x = np.arange(10)
print(x)
#multiply all elements in x by 2
x *= np.array([2])
print(x)

#advanced assignment
#update multiple values in a array with a single operator
from numpy.random import randn
rand_data = randn(3,4)
print(rand_data)
rand_data[0,2] = 100.0
print(rand_data)

#Boolean array for negative values
negatives = rand_data < 0
print(negatives)
#set all negative values to zero
rand_data[negatives]= 0  #batch assignment
print(rand_data)

#slicing
#slicing on nd.arrays return views not copies
x = list(range(10))
print(x)
slice_x = x[3:7]
print(slice_x)
slice_x[0] = 100
print(slice_x)
print(x)

#with NUMPY
x = np.arange(10)
print(x)
slice_x = x[3:7]   #this is a view of x not a copy
#slice_x = x[3:7].copy()  #this is a copy of x not a view (shallow copy(not deep))
print(slice_x) #view
slice_x[0] = 100 #this change actually effects the element in x
print(slice_x)
print(x)

#scalars can be broadcasted to slices
x[2:5] = 500
print(x)

#reshaping
x = np.arange(10)
print(x.shape)
x = x.reshape(5, 2)
print(x.shape)
print(x)

#transposing
x = x.T # 2 by 5 not 5 by 2
print(x)

#ndarray functions 
#unary ufuncs operate on a single operands
x = np.arange(10)
print(x)
print(np.sqrt(x))

#binary unfuncs operate on two operands
y = np.arange(10,20)
print(x)
print(y)
print(np.add(x, y)) #vectorized addition
print(x)
print(np.power(x, np.full(10, 2.0))) #second argument is the power, first is the number of elements
print(np.power(x, 2.0)) #without making a new array like above
