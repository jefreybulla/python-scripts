'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Examples:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

## Approach: use a sliding window of variable lenght

def minSubArrayLen(target, nums):
    # Check first element
    if nums[0] >= target :
        return 1
    # Check last element
    if nums[-1] >= target :
            return 1
    n = len(nums)
    pointer1 = 0
    pointer2 = 1
    minimal_length = float('inf')
    local_result = nums[pointer1]
    while (pointer2 < n):
        local_result += nums[pointer2]
        # print(f"pointer1: {pointer1} - pointer2: {pointer2} - local_result: {local_result}")
        if local_result >= target :
            #print('found a local solution')
            local_minimum_lenght = pointer2 - pointer1 + 1
            minimal_length = min(local_minimum_lenght, minimal_length)
            pointer1 += 1
            pointer2 = pointer1 + 1
            local_result = nums[pointer1]
            continue
        pointer2 += 1
    if minimal_length == float('inf'):
        return 0
    return minimal_length


#target = 7
#nums = [2,3,1,2,4,3] # 2

#target = 4
#nums = [1,4,4] # 1

target = 11
nums = [1,1,1,1,1,1,1,1]  # Output: 0

#target = 7
#nums = [1,1,1,1,7]

#target = 7
#nums = [8]


result = minSubArrayLen(target, nums)
print(result)
# Time complexity O(n)
