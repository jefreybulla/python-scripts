'''

Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

Examples
Input: "aa6?9"
Output: false

Input: # true
Output: true
'''


def QuestionsMarks(strParam):
    # Approach: find first two numbers. Check is 
    first_digit_seen = False
    sum = 0
    qm_counter = 0
    found_case = False
    for i in strParam:
        if i.isdigit():
            if first_digit_seen == True:
                sum += int(i)
                #print(f"i = {i} - fds = {first_digit_seen} - qmc = {qm_counter}")
                if qm_counter == 3:
                    qm_counter = 0
                    first_digit_seen = False
                    found_case = True
                    continue
                else:
                    if sum == 10 :
                        return False
                    else:
                        qm_counter = 0
                        first_digit_seen = False
                        sum = 0
                        continue
            else:
                #print(f"i = {i} - fds = {first_digit_seen} - qmc = {qm_counter}")
                sum = int(i)
                first_digit_seen = True
        if (i == '?' and first_digit_seen == True):
            #print('found a valid question mark')
            qm_counter += 1

    if found_case == False :
        return False
    
    return True

input = "aa6?9" # false
#input = "acc?7??sss?3rr1??????5"   #true 

# keep this function call here 
print(QuestionsMarks(input))
# Time complexity: O(n)
# Space complexity: O(1)


## To - do: Approach 2 - sliding windown to find pair of digits that add up to 10 and then checn the subtring between them 
# In any case approach 2 would aslo have time complexity of O(n)