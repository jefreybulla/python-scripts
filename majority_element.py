'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''


'''
Approach 1: 
Use a dictionary to keep track to numer of repetitions
'''
import time
import math

def majority_element(nums):
    d = {}
    target = { 'element': nums[0], 'repetitions': 1 }
    for num in nums:
        try:
            d[num] = d[num] + 1
            if d[num] > target['repetitions']:
                target['element'] = num
                target['repetitions'] = d[num] 
        except:
            #d[1] = 1
            d[num] = 1
    print(d)
    return target['element']



#nums = [3,2,3]
#nums = [2,2,1,1,1,2,2]
nums = [1]
#nums = [8,8,7,7,7]
result = majority_element(nums)
print(result)


'''
Approach 2: asuming odd number of elements
Get the middle element and return that value
'''

print('Approach 2')
def majority_element2(nums):
    nums.sort()
    print(nums)
    middle_element = nums[math.floor(len(nums)/2)]
    return middle_element

nums = [2,2,1,1,1,2,2]
result = majority_element2(nums)
print(result)

