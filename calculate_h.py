'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Examples:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
'''


import math
print('Approach 1')

'''
Approach 1: 
1. Sort list
2. For each element i: calculate the local_h. Keep track of max_h
'''


def calculate_h(citations):
    half_length = math.ceil(len(citations)/2)
    full_length = len(citations)
    sorted_input = sorted(citations)
    local_h = 0
    max_h = 0
    if len(citations) == 1:
        if citations[0] >= 1:
            return 1
        else:
            return 0
    for index in range(0, full_length):
        #print(f"index: {index}")
        local_h = min(len(citations) - index, sorted_input[index])
        #print(f"local_h {local_h}")
        if local_h > max_h:
            max_h = local_h
            print(f"new max_h: {max_h}")
    return max_h


#citations = [3,0,6,1,5]
citations = [0,1]
#citations = [11,15]     #2
result = calculate_h(citations)
print(result)