# Integer to roman converter


'''
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Examples:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4

Constrains
1 <= num <= 3999

'''


'''
Approach 1: 
1. Make an extended conversion dictionary that includes the basic and special cases (4,9,40,90,400,900)
2. Take input and use the largest value of the table that is less or equal to the input
3. Save roman synmbol and substract its value from input
4. Repeat steps until input is 0
'''

import time

def integer_to_roman(num):

    roman_values = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    roman_keys = roman_values.keys()
    roman_keys = list(roman_keys)
    roman_keys.reverse()
    internal_num = num
    result = ''

    while internal_num > 0:
        for key in roman_keys:
            if key <= internal_num:
                result = result + roman_values[key]
                internal_num = internal_num - key
                break
    return result

start_time = time.time()
solution = integer_to_roman(3999)
print(solution)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))


    
'''
Approach 2: 
Create a dictionary with all possible roman values from 1 to 3999
Point to solution with one call. 
Slow if we count creating the table. Fast if we consider the lookup only. 
'''
print('Approach 2')

all_roman_values = {}
for i in range(1,4000):
    all_roman_values[i] = integer_to_roman(i)

def fast_integer_to_roman(num):
    result = all_roman_values[num]
    return result

start_time = time.time()
solution = fast_integer_to_roman(3999)
print(solution)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))


'''
Approach 3
I noticed time execution improvement by changing the way I used the for loop
I used 'for i in range(len(roman_keys))' instead of 'for key in roman_keys'
'''
print('Approach 3')

def integer_to_roman3(num):

    roman_values = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    roman_keys = roman_values.keys()
    roman_keys = list(roman_keys)
    roman_keys.reverse()    # [1000, 900, ..]
    internal_num = num
    result = ''

    while internal_num > 0:
        #for key in roman_keys:
        for i in range(len(roman_keys)):
            if roman_keys[i] <= internal_num:
                result = result + roman_values[roman_keys[i]]
                internal_num = internal_num - roman_keys[i]
                break
    return result

start_time = time.time()
solution = integer_to_roman3(3999)
print(solution)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))



'''
Approach 4
As the algorithm moves to smaller numbers the comparison to large numbers are unnecesary. 
This aproach makes the for loop shorter as the algorithm moves to smaller numbers
'''
print('Approach 4')

def integer_to_roman4(num):

    roman_values = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    roman_keys = roman_values.keys()
    roman_keys = list(roman_keys)
    roman_keys.reverse()    # [1000, 900, ..]
    internal_num = num
    result = ''

    while internal_num > 0:
        #for key in roman_keys:
        for i in range(len(roman_keys)):
            if roman_keys[i] <= internal_num:
                result = result + roman_values[roman_keys[i]]
                internal_num = internal_num - roman_keys[i]
                if i > 0:
                    #remove unnecesary element
                    roman_keys.pop(0)
                break
    return result

start_time = time.time()
solution = integer_to_roman4(3999)
print(solution)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))
# only saw small time improvement vs approach 3


'''
Approach 5
Check for keys multiples to save some of the for loops. 
'''
print('Approach 5')

def integer_to_roman5(num):

    roman_values = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    roman_keys = roman_values.keys()
    roman_keys = list(roman_keys)
    roman_keys.reverse()    # [1000, 900, ..]
    internal_num = num
    result = ''

    while internal_num > 0:
        #for key in roman_keys:
        for i in range(len(roman_keys)):
            if roman_keys[i] <= internal_num:
                # save loop passes if input is a multiple of keys
                multiples_of_key = internal_num // roman_keys[i]
                if multiples_of_key > 1:
                    for j in range(multiples_of_key):
                        result = result + roman_values[roman_keys[i]]
                        internal_num = internal_num - roman_keys[i]
                else:
                    result = result + roman_values[roman_keys[i]]
                    internal_num = internal_num - roman_keys[i]
                if i > 0:
                    #remove unnecesary element
                    roman_keys.pop(0)
                break
    return result

start_time = time.time()
solution = integer_to_roman5(3999)
print(solution)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))
# Fastest of all!!!