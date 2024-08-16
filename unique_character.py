# Return the first unuqie character in a string. If there is no unique character return -1
# Approach: split string into elements of an array, iterate over elements saving number of ocurrences.abs

def getUniqueCharacter(s):
    list_s = list(s)
    #print(list_s)
    results = {}
    for i in range(0, len(list_s)):
        try:
            results[list_s[i]] += 1
        except KeyError:
            results[list_s[i]] = 1
    #print(results)
    for i in results:
        #print(i)
        if results[i] == 1:
            return i
    return -1

s = 'abacabad'
s = 'oouu'
print(getUniqueCharacter(s))