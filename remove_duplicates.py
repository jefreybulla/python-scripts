'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

import time

nums = [1,1,2,2,2,3,3,4,5,5,5,6]

print(nums)

# strategy 1: use a dictionary to store keys as the values and counts as the keys
start_time = time.time()
d = {}
for i in range(len(nums)):
    d[nums[i]] = 1

k = len(d.keys())
solution = list(d.keys())
print('solution')
print(solution)
print(k)
end_time = time.time()
print(end_time - start_time)


# strategy 2: change value of duplicates to a value I don't care about (>100) then sort
print('strategy 2')
n2 = [1,1,2,2,2,3,3,4,5,5,5,6]
start_time = time.time()
duplicates_count = 0
for i in range(len(n2)-1):
    if n2[i] == n2[i+1]:
        n2[i] = 101
        duplicates_count = duplicates_count+1
n2 = sorted(n2)
print(n2)
k = len(n2) - duplicates_count
print(k)
end_time = time.time()
print(end_time - start_time)

'''
# strategy 3: 
Use a pointer that checks every element. 
When finding that next element is duplicate, shift element left changing its value to a value I don't care
O(n)
'''
print('strategy 3')
def remove_duplicates(nums):
    pointer = 0
    initial_length = len(nums)
    duplicates_count = 0
    while pointer < initial_length -1:
        if initial_length == 1:
            return 1
        if nums[pointer] == 'X':
            break
        if nums[pointer] == nums[pointer + 1]:
            nums.pop(pointer)
            nums.append('X')
            #print(nums)
            duplicates_count = duplicates_count + 1
        else:
            pointer = pointer + 1
    return initial_length - duplicates_count


nums = [1,1,2,2,2,3,3,4,5,5,5,6] 
#nums = [1,2]
start_time = time.time()
result = remove_duplicates(nums)
print(result)
end_time = time.time()
print(end_time - start_time)
# Fastest strategy!


'''
# strategy 4: 
Assuming list includes consecutive integers:
Find the location of the next integer, then remove all elements between the next and current integer since they will be integers. 
'''
print('strategy 4')


def remove_duplicates4(nums):
    pointer1 = 0
    pointer2 = 0
    max_integer = max(nums)
    min_integer = min(nums)
    duplicates_count = 0
    initial_length = len(nums)
    while pointer1 < initial_length -1:
        # handle input such as [1, 1]
        if max_integer == min_integer:
            return 1
        try:
            # find the index of the next integer
            pointer2 = nums.index(nums[pointer1] + 1)
        except:
            # integer is the last of the list
            return pointer1 + 1
        round_duplicates_count = pointer2 - pointer1 - 1
        while round_duplicates_count > 0:
            nums.pop(pointer1+1)
            #nums.append('X')
            round_duplicates_count = round_duplicates_count - 1
            duplicates_count = duplicates_count + 1
        pointer1 = pointer1 + 1
    return(initial_length - duplicates_count)
    


nums = [1,1,2,2,2,3,3,4,5,5,5,6] 
#nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [0,0,0,0,1]
start_time = time.time()
result = remove_duplicates4(nums)
print(nums)
print(result)
end_time = time.time()
print(end_time - start_time)