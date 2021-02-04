#!/usr/bin/env python
# coding: utf-8

# # Numpy
# - core library for scientific and numerical computing in python
# - linear algebra, Fourier Transform
# - provides high performance multidimensional array object and tools for working with arrays
# - main object  is the multidimensional array
# - t is a table of elements (usually numbers) , of same data type, indexed by a tuple of positive integers
# - dimensions = axes
# - numpy arrays aka ND arrays

# ### Why Numpy and not lists?
# - Fast - have been optimized for years and thus implementation is quick
# - Convienient - has different libraries from python lists and more no. of functionalities
# - Less Memory

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3])
print(a)
a


# ### Advantage over lists

# In[3]:


import time
import sys


# In[4]:


List = range(1000) # b is a list with the range 1000 from 0 to 999
print(sys.getsizeof(6) * len(List))


# In[5]:


Numpy_Array = np.arange(1000)
print(Numpy_Array.size * Numpy_Array.itemsize)


# In[6]:


size = 20000


# In[7]:


List1 = range(size)
List2 = range(size)
Numpy_Array1 = np.arange(size)
Numpy_Array2 = np.arange(size)


# In[8]:


start = time.time()
result = [(x+y) for x , y in zip(List1, List2)]
print("Execution Time For python list :" , (time.time() - start) * 1000)


# In[9]:


start = time.time()
result = Numpy_Array1 + Numpy_Array2
print("Time for Numpy Array : " , time.time() - start * 1000)


# ## Creating Numpy Arrays

# In[10]:


numpy_array = np.array([[1,3], [3,4], [5,6]])
print("\n A numpy array: \n" , numpy_array)
print("\n Type : ", type(numpy_array))
print("\n Dtype : " , numpy_array.dtype)
print("\n NDim : " , numpy_array.ndim) # Dimensions of numpy array
print("\n ItemSize : " , numpy_array.itemsize) # size of a single element in the numpy array
'''Shape of numpy array in (rows,columns)the shape of an array is a tuple of integers giving the size of the array along each dimension.'''
print("\n Shape : " , numpy_array.shape)
print("\n NBytes : " , numpy_array.nbytes)


# In[11]:


# TypeCasting
b = 8
print(b)
b = float(b)
print(type(b))
print(b)


# In[12]:


#Typecasting of numpy arrays
arr_fl = np.array([[1,2], [3,4], [5,6]] , dtype = np.float64)
print(" A Float Array: \n" , arr_fl)
arr_comp = np.array([[1,2], [3,4], [5,6]] , dtype = np.complex)
print(" A Complex Array: \n" , arr_comp)


# In[13]:


#Automatic upcasting
a = np.array([[1.4, 8],[3,4], [5,6]])
print(a)
print(a.dtype)
print(type(a))


# In[14]:


# Initialize all the elements of the numpy array with 0
zero_array = np.zeros((5,5))
print(zero_array)


# In[15]:


# Initialize all the elements of the numpy array with 1
ones_array = np.ones((4,3))
print(ones_array)


# In[16]:


#Array filled with
full_array = np.full((4,3), 2.5)
print(full_array)


# In[17]:


l = range(5)
print("A list with range 5 : " , l)
A = np.arange(5)
print("An array with range 5 : " , A)


# In[18]:


#Array with arange() function
arange_array = np.arange(0, 20, 2)
print(arange_array)


# In[19]:


#An array with 10 values evenly distributed between 1 amd 3
lin_arr = np.linspace(1,3,10)
print(lin_arr)


# In[20]:


# A 3x3 array of random values uniformly distributed between 0 and 1
ran_arr = np.random.random((3, 3))
print(ran_arr)


# In[21]:


# A 3x4 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3, 4))


# In[22]:


# A 3x3 identity matrix
np.eye(3)


# In[23]:


#An uninitialized array of 5 integers with some garbage value
np.empty(5)


# In[24]:


_1D = np.random.randint(10, size=6) 
_2D = np.random.randint(10, size=(3, 4)) 
_3D = np.random.randint(10, size=(3, 4, 5))
print("One-dimensional array: \n" , _1D)
print("Shape:",_1D.shape, " Size:",_1D.size, " NDim:",_1D.ndim, " itemsize:",_1D.itemsize)
print("Two-dimensional array: \n" , _2D)
print("Shape:",_2D.shape, " Size:",_2D.size, " NDim:",_2D.ndim, " itemsize:",_2D.itemsize)
print("Three-dimensional array: \n" , _3D)
print("Shape:",_3D.shape, " Size:",_3D.size, " NDim:",_1D.ndim, " itemsize:",_3D.itemsize)


# ### Numpy with strings

# In[25]:


# Concatenation row-wise
print(np.char.add(['ab'],['cd']))

arr_1 = np.array((['abc', 'xyz'], ['hi','hello']))
print("\n Original Array 1 : \n" , arr_1)
print("Shape:",arr_1.shape, " Size:",arr_1.size, " NDim:",arr_1.ndim, " itemsize:",arr_1.itemsize)

arr_2 = np.array([['123'] , ['456']])
print("\n Original Array 2 : \n" , arr_2)
print("Shape:",arr_2.shape, " Size:",arr_2.size, " NDim:",arr_2.ndim, " itemsize:",arr_2.itemsize)

concat_arr = np.char.add(arr_1 , arr_2)
print("\n Concatenated Array : \n" , concat_arr)
print(" Shape:",concat_arr.shape, " Size:",concat_arr.size, " NDim:",concat_arr.ndim, " itemsize:",concat_arr.itemsize)


# In[26]:


#Replication of array elements
print(np.char.multiply('Hello ' , 4))

arr_1 = np.array((['abc', 'xyz'], ['hi','hello']))
print("\nOriginal Array : \n" , arr_1)
print("Shape:",arr_1.shape, " Size:",arr_1.size, " NDim:",arr_1.ndim, " itemsize:",arr_1.itemsize)

repl_arr = np.char.multiply(arr_1 , 3)
print("\nReplicated Array : \n" , repl_arr)
print("Shape:",repl_arr.shape, " Size:",repl_arr.size, " NDim:",repl_arr.ndim, " itemsize:",repl_arr.itemsize)


# In[27]:


print(np.char.center(['hello'] , 30))

char = np.array([['HBO'], ['Netflix'], ['Amazon Prime']])
print("\nOriginal Array : \n" , char)
print("Shape:",char.shape, " Size:",char.size, " NDim:",char.ndim, " itemsize:",char.itemsize)

char_center = np.char.center(char , 20 , fillchar = '~')
print("\nAfter .center Array : \n" , char_center)
print("Shape:",char_center.shape, " Size:",char_center.size, " NDim:",char_center.ndim, " itemsize:",char_center.itemsize)


# In[28]:


print(np.char.capitalize('i am going to market.'))

word = np.array([['men will be men', 'Imperial blue'], ['think different' , 'apple'], ['designed for drivng pleasure', 'BMW']])
print("\nOriginal Array : \n" , word)
print("Shape:",word.shape, " Size:",word.size, " NDim:",word.ndim, " itemsize:",word.itemsize)

word_cap = np.char.capitalize(word)
print("\nAfter .capitalize Array : \n" , word_cap)
print("Shape:",word_cap.shape, " Size:",word_cap.size, " NDim:",word_cap.ndim, " itemsize:",word_cap.itemsize)


# In[29]:


print(np.char.title('python classes'))

word = np.array([['men will be men', 'Imperial blue'], ['think different' , 'apple'], ['designed for drivng pleasure', 'BMW']])
print("\nOriginal Array : \n" , word)
print("Shape:",word.shape, " Size:",word.size, " NDim:",word.ndim, " itemsize:",word.itemsize)

word_ti = np.char.capitalize(word)
print("\nAfter .capitalize Array : \n" , word_ti)
print("Shape:",word_ti.shape, " Size:",word_ti.size, " NDim:",word_ti.ndim, " itemsize:",word_ti.itemsize)


# In[30]:


print(np.char.lower(['HELLO', 'WORLD']))
print(np.char.lower(['HI']))

print(np.char.upper(['hello', 'world']))
print(np.char.upper(['hello world']))


# In[31]:


print(np.char.split(['Hey there how are you ?']))

word = np.array([['men will be men', 'Imperial blue'], ['think different' , 'apple'], ['designed for drivng pleasure', 'BMW']])
print("\nOriginal Array : \n" , word)
print("Shape:",word.shape, " Size:",word.size, " NDim:",word.ndim, " itemsize:",word.itemsize)

word_split = np.char.split(word)
print("\nAfter .split Array : \n" , word_split)
print("Shape:",word_split.shape, " Size:",word_split.size, " NDim:",word_split.ndim, " itemsize:",word_split.itemsize)


# In[32]:


print(np.char.splitlines('Hello\nHow you doing?'))


# In[33]:


print(np.char.strip(['Well', 'When', 'HoW'], 'W'))

string = np.array([['red', 'rome'], ['rain' , 'drain'], ['drape', 'bear']])
print("\nOriginal Array : \n" , string)
print("Shape:",string.shape, " Size:",string.size, " NDim:",string.ndim, " itemsize:",string.itemsize)

word_strip = np.char.strip(string, 'r')
print("\nAfter .strip Array : \n" , word_strip)
print("Shape:",word_strip.shape, " Size:",word_strip.size, " NDim:",word_strip.ndim, " itemsize:",word_strip.itemsize)


# In[34]:


print(np.char.join([':' , '-'] , ['dmy', 'ymd']))


# In[35]:


print(np.char.replace('He is coding.' , 'is' , 'was'))

sentence = np.array([['He wants to be a traveller.', 'He travels.'], ['He paints.' , 'He wants to be a painter.']])
print("\nOriginal Array : \n" , sentence)
print("Shape:",sentence.shape, " Size:",sentence.size, " NDim:",sentence.ndim, " itemsize:",sentence.itemsize)

replace_ = np.char.replace(sentence, 'wants to be', 'is now')
print("\nAfter .replace Array : \n" , replace_)
print("Shape:",replace_.shape, " Size:",replace_.size, " NDim:",replace_.ndim, " itemsize:",replace_.itemsize)


# # Array Manipulation

# In[36]:


arr1 = np.arange(9)
print('Array:\n' , arr1)
print("Shape:",arr1.shape, " Size:",arr1.size, " ndim:",arr1.ndim, " itemsize:",arr1.itemsize, " dtype:",arr1.dtype)


# In[37]:


arr2 = np.array([range(i, i+3) for i in [9,3,5]])
print('Array:\n' , arr2)
print("Shape:",arr2.shape, " Size:",arr2.size, " ndim:",arr2.ndim, " itemsize:",arr2.itemsize, " dtype:",arr2.dtype)


# ### Array Indexing : Accessing Single Elements
# 

# In[38]:


# In one-dimensional array
print('arr1[5]: ',arr1[5])
print('arr1[-5] :',arr1[-5])
#In Multidimensional Array
print('arr2[2,1] :',arr2[2,1])
print('arr2[2,-1] :',arr2[2,-1])


# In[39]:


slic = slice(2,8,2)
#arr_slice = arr1[slic]
#print(arr_slice)


# In[40]:


# Modifying values
arr2[0,0] = 20
print("After modifiction: \n",arr2)
arr1[4] = 8.45
print("After updation: \n",arr1)


# ### Array Slicing : Accessing Subarrays

# In[41]:


# One-dimensional array
print('arr1[ : 5] :',arr1[ : 5])
print('arr1[4 : 7] :',arr1[4 : 7])
print('arr1[1 : : 2] :',arr1[1::2])
print('arr1[ : : -1] :',arr1[ : :-1])
print('arr1[5 : : -2] :',arr1[ : :-2])


# In[42]:


#Two-Dimensional Array
print('arr2[[ : 2, : 3] :\n',arr2[:2, :3]) #2 rows, 3cols
print('arr2[ : 3, : : 2] :\n',arr2[:3, ::2]) #allrows, evry ither col
print('arr2[ : :-1, : : -1] :\n',arr2[::-1, ::-1]) #Reversing


# In[43]:


#Combining Indexing and Slicing
print('arr2[:, 0] :',arr2[:, 0]) #first column
print('arr2[0, :] :',arr2[0, :]) #first row
print('arr2[0] :',arr2[0])


# In[44]:


print("Original array : \n" , arr2)
sub_arr2 = arr2[:2, :2]
print("Sub Array : arr2[:2, :2] \n" , sub_arr2)
sub_arr2[0, 0] = 99
print("Modified Sub Array : \n" , sub_arr2)


# In[45]:


sub_arr2_copy = sub_arr2[:2, :2].copy()
print('sub_arr2_copy: \n',sub_arr2_copy)
sub_arr2_copy[0, 0] = 42
print('After modification sub_arr2_copy: \n', sub_arr2_copy)
print('After modification sub_arr2: \n', sub_arr2)


# # Reshaping Array
# - the size of the initial array must match the size of the reshaped array

# In[46]:


array = np.arange(1,10)
print("Array originally: " , array)
ar_res = array.reshape(3,3)
print('Reshaped Array:\n' , ar_res)
print("Shape:",ar_res.shape, " Size:",ar_res.size, " ndim:",ar_res.ndim, " itemsize:",ar_res.itemsize, " dtype:",ar_res.dtype)


# ### Reshaping 1D array into a 2D array

# In[47]:


print("Row vector using reshape: ", array.reshape((1,9)))
print("Row vector using newaxis: ", array[np.newaxis, :])
print("Column vector using reshape: \n", array.reshape(9,1))
print("Column vector using newaxis: \n", array[: ,np.newaxis])


# In[48]:


flat_arr = ar_res.flatten()
print('Flattened Array:\n' , flat_arr)
print("Shape:",flat_arr.shape, " Size:",flat_arr.size, " ndim:",flat_arr.ndim, " itemsize:",flat_arr.itemsize, " dtype:",flat_arr.dtype)


# In[49]:


col_flat_arr = ar_res.flatten(order = 'F')
print('Column wise Flattened Array:\n' , col_flat_arr)
print("Shape:",col_flat_arr.shape, " Size:",col_flat_arr.size, " ndim:",col_flat_arr.ndim, " itemsize:",col_flat_arr.itemsize, " dtype:",col_flat_arr.dtype)


# In[50]:


trans_arr = np.transpose(ar_res)
print('Transpose of Array:\n' , trans_arr)
print("Shape:",col_flat_arr.shape, " Size:",col_flat_arr.size, " ndim:",col_flat_arr.ndim, " itemsize:",col_flat_arr.itemsize, " dtype:",col_flat_arr.dtype)


# In[51]:


print('reshape(2,6)- \n', np.arange(12,24).reshape(2,6))
# no. of arrays, no. of rows, no. of columns
print('reshape(2,3,2)- \n',np.arange(12,24).reshape(2,3,2))


# # Numpy Arithmetic Operations

# In[52]:


a = np.arange(9).reshape(3,3)
a


# In[53]:


b = np.array([10,11,12])
b


# In[54]:


c = np.array([[3, 4 ,5],[6,7,8],[1,2,3]])
np.add(a,c)


# In[55]:


np.add(a,b)


# In[56]:


print(np.subtract(a,b))
print(np.subtract(a,c))


# In[57]:


print(np.multiply(a,b))
print(np.multiply(a,c))


# In[58]:


print(np.divide(a,b))


# ##### Iteration over array

# In[59]:


a = np.arange(0, 45, 5)
a


# In[60]:


a = a.reshape(3,3)


# In[61]:


for x in np.nditer(a):
    print(x)


# In[62]:


print(a)
for x in np.nditer(a, order = 'C'):
    print(x)
    
for x in np.nditer(a, order = 'F'):
    print(x)


# # Joining Arrays
# - pass a tuple or list of arguments to be concatenated

# In[63]:


# Joining 1D arrays
print(np.concatenate([[1,2,3],[4,5,6],[0,0,0]]))
# Joining 2D arrays
a = np.array([[1,2], [3,4]])
print("Array 1- \n", a)
print('Joining 1 & 1- \n' , np.concatenate((a,a)))
b = np.array([[5,6], [7,8]])
print("Array 2 - \n" , b)
print('Joining 1 & 2- \n' , np.concatenate((a,b)))
c = np.array([[0,0],[1,1]])
print("Array 3 - \n" , c)
print('Joining 1, 2 & 3- \n' , np.concatenate((a,b,c)))


# In[64]:


print("Concatenating along column or second axis- \n" , np.concatenate((a,b),axis = 1))


# In[65]:


a1 = np.array([1,2,3])
a2 = np.array([[0,0,0],[3,2,1]])
a3 = np.array([[0], [4]])
a4 = np.array([[9,8,7],[4,5,6]])
print("a1: \n", a1)
print("a2: \n", a2)
print("a3: \n", a3)
print("a4: \n", a4)

# To vertically stack the arrays
print("Vertical Stack: \n", np.vstack([a1,a2]))

# To horizontally stack the arrays
print("Horizontal Stack: \n", np.hstack([a3,a2]))

# To stack along the third dimension
print("Stack aong 3rd axis: \n", np.dstack([a2, a4]))


# # Splitting Arrays

# In[66]:


a5 = [11, 62, 73, 99, 99, 33, 22, 10]
a6 = np.arange(1,17).reshape((4, 4))
a7 = np.arange(1,13).reshape(3,2,2)
print("a1: \n", a5)
print("a4: \n", a6)
print("a7: \n", a7)
# n split points = n+1 subarrays
print("Split a5 [2,5]: \n", np.split(a5,[2,5]))
print("Vertical Split: \n", np.vsplit(a6, [2]))
print("Horizontal Split: \n", np.hsplit(a6, [2]))
print("Split along 3rd axis: \n", np.dsplit(a7, [2,2]))


# ### Resizing an Array

# In[67]:


a = np.array([[1,2,3] , [4,5,6]])
print(a)
print(a.shape)
b = np.resize(a , (3,2))
print(b)
print(b.shape)


# In[68]:


b = np.resize(a, (3,3))
print(b)
print(b.shape)


# In[69]:


#Histogram


# In[70]:


import  matplotlib.pyplot as plt
a = np.array([ 20, 6, 42, 90, 96, 62, 87, 15, 7, 71, 56, 43, 21, 54, 88, 66])
plt.hist(a, bins = [0, 20, 40, 60, 80, 100])
plt.title('Histogram')
plt.show()


# In[71]:


plt.hist(a, bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.show()


# In[ ]:




