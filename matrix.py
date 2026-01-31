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

# Matrix operations
print('# matrix multiplication')
x = numpy.array([[1,2],[2,3],[3,4.9]])      # 3x2 matrix
m = numpy.array([[2],[3.3]])                # 2x1 matrix
print(x @ m)        # results on a 3x1 matrix

print('# boardcasting operation #')
# matrix size is not compatible but numpy broadcast the operation on all three rows (transpose is necessary):
# substract 2 to every elements of the first columns
# substract 3.3 to every element of the second columns
result = x - m.T
print(result)
print('# multiply a matrix with its transposed #')
result_transposed = result.T
multiplied = result_transposed @ result
print( multiplied )

print('# adding a matrix to itself #')
multiplied += multiplied
print(multiplied)

print('# inverse of a matrix #')
inverse = numpy.linalg.inv(multiplied)
print(inverse)

print('######')
b = numpy.array([[1, -1],[-1, 1]])
c = inverse @ b     # 2x2 matrix
print(c)

print('# Eigen Results #')
# Finding eigenvalues and eigenvectors
eigen_values, eigen_vectors = numpy.linalg.eig(c)
print(eigen_values)
print(eigen_vectors)
