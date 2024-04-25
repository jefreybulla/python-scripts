'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

'''


'''
Aproach 1:  
1. Sort list
2. Traverse list to find smallest possible integer starting with 1
3. Do this until missing integer is found
'''

def missing_integer(nums):
    nums.sort()
    print(nums)
    target = 1
    while True:
        target_found = False
        for num in nums:
            if num == target:
                target += 1
                target_found = True
                break
        if not target_found:
            return target


nums = [1, 3, 6, 4, 1, 2]
result = missing_integer(nums)
print(result)




