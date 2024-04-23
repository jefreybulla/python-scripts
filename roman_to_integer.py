# Roman to integer converter



'''

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Constraints
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
It is guaranteed that s is a valid roman numeral in the range [1, 3999] [I, MMMCMXCIX]

Examples

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


single_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
combinations = { 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900 }

def roman_to_integer(s):
    result = 0
    # arrange s into singles or groups
    l = []
    input_lenght = len(s)
    skip_next = False
    for i in range(input_lenght):
        if skip_next == False:
            if i < len(s)-1 and single_values[s[i]] < single_values[s[i+1]]:
                l.append(s[i]+s[i+1])
                skip_next = True
                continue
            else:
                print('s[i]-->')
                print(s[i])
                l.append(s[i])
        skip_next = False
    print('group input ->')
    print(l)
    # decode based on singles or groups
    for i in range(len(l)):
        if len(l[i]) > 1:
            result = result + combinations[l[i]]
        else:
            result = result + single_values[l[i]]
    return result


solution = roman_to_integer('MMMCMXCIX')
#solution = roman_to_integer('III')
print(solution)
