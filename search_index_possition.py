'''
# Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

import math


# O(n) solution
def search_element(nums, target):
    for i in range(len(nums)):
        print(i)
        if target <= nums[i]:
            solution = i
            break
        if i == len(nums)-1:
            solution = i+1
    print('solution ->')
    print(solution)
    return solution

#nums = [1,3,5,7]
nums = [1,3]
target = 3
search_element(nums,target)


# O(log n solution)
print('O(log n solution ->)')
#nums = [1,3,5,6]
#nums = [1,2,3,4,5]
nums = [1,3,5,6,8,10,11,15]
target = 14

skipped_elements = 0

def slice_search(list_input):
    # global allows this function to modify skippped_elements
    # Alternatively I can add it as a fucntion argument: slice_search(list_input, skipped_elements)
    global skipped_elements
    middle_pointer = math.floor((len(list_input))/2)
    print(type(middle_pointer))
    print(middle_pointer)
    # solution is the middle element
    if target == list_input[middle_pointer]:
        print('solution found!')
        solution = middle_pointer + skipped_elements
        print(solution)
        return solution
    #search left side of list
    elif target <= list_input[middle_pointer]:
        sublist = list_input[:middle_pointer]
        print(sublist)
    # search right side of list
    else:
        sublist = list_input[middle_pointer:len(list_input)]
        print(sublist)
        skipped_elements = skipped_elements + middle_pointer
    if len(sublist) <=3:
        solution = search_element(sublist, target) + skipped_elements
        print('solution found!')
        print(solution)
        return solution
    else:
        return slice_search(sublist)

s = slice_search(nums)
print(s)