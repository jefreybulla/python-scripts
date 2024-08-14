'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs):
    first_word = strs[0]
    if (first_word == ''):
        return ''
    n = len(strs)
    if (n == 1):
        return first_word
    j = 0
    common = ''
    while(True):
        for i in range(1,n):
            try:
                if (strs[i][j] == first_word[j]):
                    continue
                else:
                    return common
            except:
                return common
        common += first_word[j]
        j += 1 
    return common

strs = ["flower","flow","flight"]
result = longestCommonPrefix(strs)
print(result)
# Time complexity: O(n)


