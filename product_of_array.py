'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Examples:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

 
import time 

def productExceptSelf(nums):
    nums_copy = nums
    result = []
    for j in range(0, len(nums)):
        removed_element = nums_copy.pop(j)
        #print(nums_copy)
        product_result = 1
        for i in range(0, len(nums_copy)):
            product_result = product_result * nums_copy[i]
        result.append(product_result)
        nums_copy.insert(j,removed_element)
    return result


nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
start_time = time.time()
output = productExceptSelf(nums)
end_time = time.time()
print('result -->')
print(output)
print(f"execution time: {end_time - start_time}")
# This approach is slow O(n^2)




## approach 2: get total product and then use division to get the desired result
# if there is one zero, only one item of result will be non-zero value 
# if there is more than one cero, all items in result will be zero
print('Approach 2 ->>')
import numpy

def productExceptSelf2(nums):
    temp_result = 1
    zero_count = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            temp_result = temp_result * nums[i]
        else:
            zero_count += 1
            zero_index = i
            if (zero_count > 1):
                # exit with zeros
                result = [0]*len(nums)
                return result
    
    if zero_count == 1:
        result = [0]*len(nums)
        result[zero_index] = temp_result
        return result

    numpy_array = numpy.array(nums)
    result = temp_result/numpy_array
    return result.astype(numpy.int64)
    


nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
#nums = [-1,0,0,-3,3]
start_time = time.time()
output = productExceptSelf2(nums)
end_time = time.time()
print('result -->')
print(output)
print(f"execution time: {end_time - start_time}")
# This approach is faster than apprach 1. Runs in O(n)



## approach 3, creaate two new lists to store the prefix products and the suffix products
print('Approach 3 --->')

def productExceptSelf3(nums):
    n = len(nums)
    pre_item = [1] * n
    post_item = [1] * n
    result = [1] * n

    for i in range(1, n):
        pre_item[i] = nums[i-1]*pre_item[i - 1]
    #print(pre_item)
    for j in range(n-2, -1, -1):
        post_item[j] = nums[j+1] * post_item[j+1]
    #print(post_item)

    for i in range(0, n):
        result[i] = pre_item[i] * post_item[i]
    
    return result

nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
start_time = time.time()
output = productExceptSelf3(nums)
end_time = time.time()
print(output)
print(f"execution time: {end_time - start_time}")
# Aproach 3 is slower than approach 2. Both are O(n)