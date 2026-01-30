# In python arrays are different from lists. 
# You can have multidimensional array and perform math operations on array elements
# all elements in an array mush be of the same type (a list can store elements of different types)

import array as arr 

# i specifies the intefer type. Use f for float
numbers = arr.array('i',[10,20,30])

print(numbers[-1]) #gets last item

print(len(numbers))

numbers.append(40)
print(numbers)

# find index of element with value equal to 20
print(numbers.index(20))


# iterate over array
for number in numbers:
    print(number)

# another way to iterate
for i in range(len(numbers)):
    print(numbers[i])


# Slice array
print('sliceing -->')
# first two elements
print(numbers[:2])
# element second to thrid position
print(numbers[1:3])


print('removing elements -->')
# remove element that holds a specific value
numbers.remove(40)
print(numbers)
# remove element by its position
numbers.pop(1)
print(numbers)

# more examples https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/

l = [1,2,3,4,5]
print('shifting left')
l.append(l.pop(0))
print(l)
print('shifting right')
l.insert(0, l.pop())
print(l)


## Numpy arrays 
import numpy

print('Numpy arrays')
a = numpy.array([2,4,6])
print(a)
# divide each element by 2
b = a/2
print(b)
# convert each element from float to integer 
b = b.astype(numpy.int64)
print(b)

# Vectors
a_2D = numpy.array([[1, 3]])          # 2-dimensional array
print(a_2D.shape)           #(1, 2) means 1 row, two columns
a_2D_T = a_2D.T             # transpose
print(a_2D_T)
print(a_2D_T.shape)         #(2,1) is two rows, one column

# Matrices
print('- Numpy array manipulation -')
c = numpy.array([[1, 2],[3, 4],[5, 6]])
print(c[0])         # first row [1,2]
print(c[0,1])       # first row, second column (2)
print(c[:,0])       # all rows of the first column [1 3 5]
print(c[1,:])       # all columns of the second row [3 4]


# Obtaining the shape of a matrix
print('# shape of matrix #')
number_of_rows, number_of_columns = c.shape
print(f'rows: {number_of_rows}, columns: {number_of_columns}')

print('# adding elements of a matrix #')
print(c[1,:].sum())         # add all elements of row 2. 3+4 = 7

# Calculations across columns and rown
print('# computing means #')
mean_rows = c.mean(axis=0)    # take mean accross rows [(1+3+5)/3 (2+4+6)/3]           
print(mean_rows)            # [3 4]
print(mean_rows.shape)      # 2 -> 1 dimension array

mean_columns = c.mean(axis=1)    # take mean accross columns [(1+2)/2 (3+4)/2 (5+6)/2]           
print(mean_columns)            # [1.5 3.5 5.5]
print(mean_columns.shape)      # 3 -> 1 dimension array 

print('reshaping dimensions')
mean_columns = mean_columns.reshape(-1, 1)
print(mean_columns.shape)       # (3, 1) it's now a matrix with 3 rows and one column
print(mean_columns)

print('reshaping dimensions II')
mean_columns = mean_columns.reshape(1, -1)
print(mean_columns.shape)       # (1, 2) it's now a matrix with 3 columns and one row
print(mean_columns)