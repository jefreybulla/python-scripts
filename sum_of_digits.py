'''
You are given a two-digit integer n. Return the sum of its digits.
'''


def solution(n):
    n_list = list(str(n))
    sum = 0
    for item in n_list:
        sum += int(item)
    return sum


n = '29'
print(solution(n)) # 11