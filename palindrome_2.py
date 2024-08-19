'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

import re

def isPalindrome(s):
    # regular expression used to remove non-alphanumeric characters
    s_internal = re.sub(r'[^a-zA-Z0-9]', '', s)
    s_internal = s_internal.lower()
    print(s_internal)
    s_reverse = s_internal[::-1]
    if(s_reverse == s_internal):
        return True
    else:
        return False
    #print(s_internal)


#s = "A man, a plan, a canal: Panama"    #True
#s = "race a car"    # False
#s = " "         # True
s = "ab_a"      # True 

result = isPalindrome(s)
print(result)