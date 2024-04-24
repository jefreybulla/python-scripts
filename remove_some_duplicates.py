'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Examples:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''


'''
# strategy 1: 
Use a pointer that checks every element. 
When finding that next element is duplicate, shift element left changing its value to a value I don't care
O(n)
'''



print('strategy 1')
def remove_some_duplicates(nums):
    pointer = 0
    initial_length = len(nums)
    duplicates_count = 0
    while pointer < initial_length -2:
        if initial_length == 1:
            return 1
        if nums[pointer] == 'X':
            break
        if nums[pointer] == nums[pointer + 2]:
            nums.pop(pointer)
            nums.append('X')
            #print(nums)
            duplicates_count = duplicates_count + 1
        else:
            pointer = pointer + 1
    return initial_length - duplicates_count


nums = [1,1,1,2,2,3]
print(nums)
result = remove_some_duplicates(nums)
print(result)
print(nums)
