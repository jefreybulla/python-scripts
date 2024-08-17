'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''


## Approach: create numRows emty lists. Use a loop to secuencially add chars to those lists. 
# Zigzag pattern 1,2,3,...n,n-1, n-1,...1,23

def convert(s, numRows):


    if (numRows <= 1):
        return s

    len_s = len(s)
    if (len_s < numRows ):
        return s

    result_array = [''] * numRows
    
    bucket = 0
    counter = 0
    while(counter < len_s):
        while(bucket < numRows -1 ):
            try:
                result_array[bucket] += s[counter]
            except IndexError:
                break
            #print(bucket)
            bucket += 1
            counter += 1
        while(bucket > 0):
            try:
                result_array[bucket] += s[counter]
            except IndexError:
                break
            #print(bucket)
            bucket -= 1
            counter += 1
    
    result = ''
    for item in result_array:
        result += item
    
    return result


s = "PAYPALISHIRING"
numRows = 3

#s = "A"
#numRows = 1

#s = "ABC"
#numRows = 2

result = convert(s, numRows)
print(result)