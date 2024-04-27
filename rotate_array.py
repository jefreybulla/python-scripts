'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative

Examples:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''

import time

'''
Approach 1: use recursion
O(k)
'''


def rotate_to_right(nums,k):
    if k > 0:
        last_element = nums[-1]
        nums.insert(0,last_element)
        nums.pop(-1)
        k = k -1
        rotate_to_right(nums,k)
    else:
        return


nums = [1,2,3,4,5,6,7]
k = 3
start_time = time.time()
rotate_to_right(nums, k)
end_time = time.time()
print(nums)
print(end_time - start_time)


'''
Approach 2: 
Create a sublist of elements that will be roatating sl1
Create a sublist of the elements that will stay sl2
concatanate sl1 + sl2
O(1)
'''
print('Approach 2 ->')

def rotate_to_right2(input,k):
    global nums
    input_lenght = len(input)
    sl1 = input[input_lenght-k:input_lenght]
    sl2 = input[0:input_lenght-k]
    nums = sl1 + sl2
    return 

nums = [1,2,3,4,5,6,7]

k = 3
start_time = time.time()
rotate_to_right2(nums, k)
end_time = time.time()
print(nums)
print(end_time - start_time)
