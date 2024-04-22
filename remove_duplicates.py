'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''


nums = [1,1,2,2,2,3,3,4,5,5,5,6]


#nums.pop(0)

print(nums)

# strategy 1: use a dictionary to store keys as the values and counts as the keys
d = {}
for i in range(len(nums)):
    d[nums[i]] = 1

k = len(d.keys())
solution = list(d.keys())
print('solution')
print(solution)
print(k)


# strategy 2: change value of duplicates to a value I don't care about (>100) then sort
n2 = [1,1,2,2,2,3,3,4,5,5,5,6]
duplicates_count = 0
for i in range(len(n2)-1):
    if n2[i] == n2[i+1]:
        n2[i] = 101
        duplicates_count = duplicates_count+1
n2 = sorted(n2)
print(n2)
k = len(n2) - duplicates_count
print(k)
