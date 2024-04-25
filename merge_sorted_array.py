'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Examples:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

'''

import time

'''
Approach 1: 
1. For each element of nums2:
    - find the correct position in numbs1
    - pop last item of nums1
O(n*m)
'''

start_time = time.time()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


for i in range(len(nums2)):
    for j in range(len(nums1)):
        if nums2[i] < nums1[j] or j >= m+i:
            nums1.insert(j,nums2[i])
            nums1.pop()
            break

print(nums1)

end_time = time.time()
print(f"execution time: {end_time - start_time}")


'''
Approach 2: 
Two pointers: one pointer for nums1, one pointer for nums2
Pointer move from left to right comparing and adding elements to nums1 if nums2[j] < nums[i]
O(n+m)
'''

print('Approach 2')
start_time = time.time()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

pointer1 = 0
pointer2 = 0

while pointer2 <= len(nums2) - 1:
    if n == 0:
        break
    if nums2[pointer2] < nums1[pointer1] or pointer1 >= pointer2 + m:
        nums1.insert(pointer1, nums2[pointer2])
        pointer2 = pointer2 + 1
        nums1.pop()
    pointer1 = pointer1 + 1

print(nums1)

end_time = time.time()
print(f"execution time: {end_time - start_time}")
# Faster than approach 1 !!