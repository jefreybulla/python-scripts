'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Examples:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''


import time

## Approach 1: Naive approach iterating over all the possible triplets
def threeSum(nums):
    nums_copy = nums.copy()
    #nums_copy.sort()
    #print(nums_copy)
    n = len(nums_copy)
    triplets = []
    for i in range(0,n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if(i!=j and i!=k and j!=k):
                    sum = nums_copy[i] + nums_copy [j] + nums_copy[k]
                    if (sum == 0):
                        #print('triplet found!')
                        item_to_add = [nums_copy[i], nums_copy [j], nums_copy[k]]
                        item_to_add.sort()
                        if item_to_add not in triplets:
                            triplets.append(item_to_add)
    return triplets




#nums = [-1,0,1,2,-1,-4]      # [[-1,-1,2],[-1,0,1]]
#nums = [-2,0,1,1,2]         # [[-2,0,2],[-2,1,1]]

nums = [13,-11,-14,4,-9,-10,-11,7,-14,-9,14,0,-5,-7,6,-9,11,6,-14,-12,-10,9,-8,-7,5,6,8,-12,-1,-4,14,-3,0,7,9,7,12,13,-9,13,11,-10,-10,-9,-10,12,-10,8,-5,13,11,-8,7,-12,0,-11,2,-14,-8,8,-3,13,-9,5,5,7,-11,-6,5,-13,-7,1,14,-10,-1,-11,-13,4,12,-11,2,0,-4,-14,4,4,-10,13,-3,-10,6,1,-12,4,-9,1,-4,-13,10,8,-11,10,-14,-12,-14,1,-8,10,-10,11,-15,0,-3,-12,1,-14,-1,-1,6,11,-4,-3,-2,-1,-13]

start = time.time()
result = threeSum(nums)
finish = time.time()
print(result)
print(f"Time of execution: {finish - start}")   # 0.036485910415649414
# Time complexity: O(n^3)

## Approach 2: for each element: create a new array without that elements and resolve it as a two sum problem!
print ('Approach 2 -->')

def threeSum2(nums):
    nums.sort()
    #print('sorted input ->')
    #print(nums)
    n = len(nums)
    
    triplets = []
    memory_elements_removed = []
    for i in range(0, n):
        nums_copy = nums.copy()
        element_removed = nums_copy.pop(i)
        if element_removed in memory_elements_removed :
            #print('skipping this loop')
            continue
        memory_elements_removed.append(element_removed)
        
        # Two sum problem from now on
        target = -1 * element_removed
        m = len(nums_copy)
        pointer1 = 0
        pointer2 = m - 1

        while(pointer1 < pointer2):
            sum = nums_copy[pointer1] + nums_copy[pointer2]
            if sum == target :
                #print('triplet found')
                item_to_add = [element_removed, nums_copy[pointer1], nums_copy[pointer2]]
                item_to_add.sort()
                if item_to_add not in triplets :
                    triplets.append(item_to_add)
                pointer1 += 1
            if sum < target :
                pointer1 += 1
                continue
            if sum > target :
                pointer2 -= 1
    return triplets

#nums = [-1,0,1,2,-1,-4]      # [[-1,-1,2],[-1,0,1]]
#nums = [-2,0,1,1,2]         # [[-2,0,2],[-2,1,1]]


start = time.time()
result = threeSum2(nums)
finish = time.time()
print(result)
print(f"Time of execution: {finish - start}")   # 0.001965045928955078 order of magnitude faster!!
# Time complexity O(n^2)
