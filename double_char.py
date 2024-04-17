# Create a function that takes a string and returns a string in which each character is repeated once.
# Examples
# double_char("String") ➞ "SSttrriinngg"
# double_char("Hello World!") ➞ "HHeelllloo WWoorrlldd!!"

def double_char(txt):
    return ''.join([i*2 for i in txt])

print(double_char("String"))

