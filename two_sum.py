'''
Create an algorithm that given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Examples 1
Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 
Example 2:
Input: nums = [3,2,4], target = 6 Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6 Output: [0,1]
'''

nums = [3,2,4]
print(len(nums))
target = 6
solution = []
found_solution = False

print('running...')
for i in range((len(nums))-1):
    for j in range(i+1,len(nums)):
        if i != j:
            if nums[i]+nums[j] == target:
                solution = [i,j]
                found_solution = True
                break
            
    if found_solution:
        break

print(solution)
# Execution time: 2,729 ms


# Faster algorithm:
#To solve this problem, you can use a dictionary to store the numbers in the list as keys and 
# their indices as values. Then, for each number, you can check if the difference between the
# target and the current number is already in the dictionary. If it is, you have found the two
# numbers that add up to the target. Here's the Python code for this algorithm:


# Execution time: 36 ms
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i


print(two_sum(nums, target))