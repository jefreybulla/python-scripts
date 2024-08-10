'''
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Examples

Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation: 
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.


Input: version1 = "1.01", version2 = "1.001"
Output: 0

Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation:
version1 has less revisions, which means every missing revision are treated as "0".
'''


## Aproach: Split string. Make sure the result arrays have the same length. Compare from left to right

import numpy

def compareVersion(version1, version2):
    v1_array = version1.split('.')
    v2_array = version2.split('.')

    n1 = len(v1_array)
    n2 = len(v2_array)


    n_max = max(n1, n2)

    if (n1 < n_max):
        for i in range(0, n_max-n1):
            v1_array.append('0')
    if (n2 < n_max):
        for h in range(0, n_max-n2):
            v2_array.append('0')

    for j in range(0, n_max):
        if(int(v1_array[j])>int(v2_array[j])):
            return 1
        if(int(v1_array[j])<int(v2_array[j])):
            return -1
    return 0




#version1 = "1.02"
#version2 = "1.10.3"

version1 = "1.0.1"
version2 = "1"


result = compareVersion(version1, version2)
print(result)
# Time complexity: O(n)