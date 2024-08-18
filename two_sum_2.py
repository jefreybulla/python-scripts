'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Examples
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

def twoSum(numbers,target):
    pointer1 = 0
    pointer2 = len(numbers) - 1

    solution_found = False

    while (solution_found == False):
        sum = numbers[pointer1] + numbers[pointer2]
        if (sum == target):
            solution_found
            break
        if(sum < target):
            pointer1 += 1
            continue
        if(sum > target):
            pointer2 -= 1        

    return [pointer1 + 1, pointer2 + 1]


#numbers = [2,7,11,15]
#target = 9  
# Output [1,2]

#numbers = [2,7,11,1]
#target = 3 
# Output [1,4]

numbers = [2,3,4]
target = 6
#Output: [1,3]

result = twoSum(numbers, target)
print(result)

