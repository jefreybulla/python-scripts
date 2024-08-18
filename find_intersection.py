'''
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.

Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
'''

# Approach: use a dictionary to check duplicates

def FindIntersection(strArr):
    str0 = strArr[0].split(', ')
    str1 = strArr[1].split(', ')
    intersection_counter = {}
    for i in str0:
        try:
            intersection_counter[i] += 1
        except:
            intersection_counter[i] = 1
    for i in str1:
        try:
            intersection_counter[i] += 1
        except:
            intersection_counter[i] = 1
    print('intersection_counter')
    print(intersection_counter)
    result = []
    for i in intersection_counter:
        if (intersection_counter[i] > 1):
            result.append(i)

    if (len(result) == 0):
        return False
    # code goes here
    return ",".join(result)

# input =["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] # 1,4,13
input = ["1, 5, 6, 7, 10, 11, 12", "5, 6, 8, 11, 17"]   # 5,6,11
#input = ["1, 2, 3, 4, 5", "6, 7, 8, 9, 10"]     # false

print(FindIntersection(input))