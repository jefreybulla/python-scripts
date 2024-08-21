'''
Given a string s, find the length of the longest 
substring without repeating characters.

Examples
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''



def lengthOfLongestSubstring(s):
    n = len(s)
    if n == 1 :
        return 1
    if n == 0 :
        return 0
    pointer = 1

    max_lenght = 1
    local_unique_substring = s[0]
    while(pointer < n ):
        #print(f"pointer= {pointer} - s[pointer]= {s[pointer]} - local_s= {local_unique_substring}")
        if (s[pointer] not in local_unique_substring):
            #print('found unique')
            local_unique_substring += s[pointer]
            #print(f"pointer= {pointer} - s[pointer]= {s[pointer]} - local_s= {local_unique_substring}")
            max_lenght = max(max_lenght, len(local_unique_substring))
            pointer += 1
        else:
            #print('found NOT unique')
            last_seen_at_index = local_unique_substring.find(s[pointer])
            number_of_elements_to_remove = last_seen_at_index + 1
            local_unique_substring = local_unique_substring[ number_of_elements_to_remove:] + s[pointer]
            #print(local_unique_substring)
            pointer += 1

    return max_lenght


s = "abcabcbb"  # Output: 3
#s = "aba"   # 2
#s = "aas"   # 2
#s = "bbbbb"     #1
#s = "pwwkew"    #3
#s = "dvdf"  #3 
#s = "anviaj"    #5

result = lengthOfLongestSubstring(s)
print(result)
# time complexity: O(n)
# Space complexity: O(1) only a fix space in memory needed to store local_unique_substring and counters