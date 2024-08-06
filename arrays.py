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
a2 = a/2
print(a2)
# convert each element from float to integer 
a2 = a2.astype(numpy.int64)
print(a2)
