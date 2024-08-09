'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.


Examples:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''

## Approach 1: traverse right then left 

import numpy


def candy(ratings):
    n = len(ratings)
    candy_needed = [1]*n

    #candy_tr_right = [0]*n
    #candy_tr_left = [0]*n

    # traverse from left to right 

    #extra_candy = 1

    for i in range(1, n):
        if(ratings[i]>ratings[i-1]):
            candy_needed[i] = candy_needed[i-1] + 1
    # traverse right to left
    for j in range(n-2,-1,-1):
        if(ratings[j]>ratings[j+1]):
            if (candy_needed[j] <= candy_needed[j+1]):
                candy_needed[j] = candy_needed[j+1] + 1
    result = sum(candy_needed)
    
    return result



#ratings = [1,0,2]
#ratings = [1,2,2]
#ratings = [1,3,2,2,1]
#ratings = [1,2,87,87,87,2,1]
ratings = [1,3,4,5,2]

result = candy(ratings)
print(result)
# Time complexity: O(n)
