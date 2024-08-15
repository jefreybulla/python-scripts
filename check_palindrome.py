'''
Given the string, check if it is a palindrome (it reads the same backward and forward)
'''


def solution(inputString):
    # reverse string
    reverse = inputString[::-1]
    return reverse == inputString



inputString = 'noonm'

print (solution(inputString)) # True