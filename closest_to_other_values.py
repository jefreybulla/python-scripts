'''
Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)

'''


def solution(a):

    indexOfMinimum = -1
    
    # unbounded upper value for comparison. Useful for finding lowest values
    minimalSum = float('inf')

    for i in range(len(a)):
        curSum = 0
        for j in range(len(a)):
            curSum += abs(a[i] - a[j])
        if curSum < minimalSum:
            minimalSum = curSum
            indexOfMinimum = i

    return a[indexOfMinimum]


a = [2, 4, 7]
#a = [1, 1, 3, 4]

print(solution(a))