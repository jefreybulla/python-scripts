'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.


Examples:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

'''

import math


## Try this next:
# Since I need the concept of words to fill up spaces, it would be better to use words from the beginning:
# Get the first word and align it -> fill up rest of available space with spaces
# Get second word and align it -> check if word can be in the same line and calculate spaces
# Do this until all words have been aligned

def fullJustify(words, maxWidth):
    word_pointer = 0
    total_words = len(words)
    current_line = 0
    number_of_words_in_line = 0
    # minimum_spaces_in_line this could be calculate as (number_of_words_in_line - 1)
    words[word_pointer]
    result_array = ['']
    result_line = 0
    current_words = []
    # current_words_len stores the lenght of all non-space words in array
    current_words_len = 0

    def can_word_fit(current_words_len, new_word_len, number_of_words_in_line):
        if (current_words_len == 0):
            return True

        # number_of_words_in_line - 1 is the numer of spaces needed. 
        # However we updated number of words is + 1 when counting the new word, hence the follwoing:

        minimum_spaces_in_line = number_of_words_in_line

        space_left = maxWidth - current_words_len - new_word_len - minimum_spaces_in_line
        if (space_left >= 0):
            return True
        return False

    def align(current_words, current_words_len, number_of_words_in_line, last_word):
        number_of_space_slots = number_of_words_in_line - 1
        space_left = maxWidth - current_words_len

        if (number_of_words_in_line <= 1):
            return current_words[0] + ' ' * space_left

        if (last_word):
            return " ".join(current_words) + ' ' * (space_left - number_of_words_in_line + 1)

        # Create space slots content
        space_slots_content = [''] * number_of_space_slots
        #left_for_spaces = space_left
        number_of_slots_remaining = number_of_space_slots
        for i in range(0, number_of_space_slots):
            current_slot_len = math.ceil(space_left/number_of_slots_remaining)  #4
            space_slots_content[i] = " " * current_slot_len
            space_left -= current_slot_len  # 4
            number_of_slots_remaining -= 1  #1
        
        # fill in the spaces between words
        words_copy = current_words.copy()
        content_array_with_spaces = []

        slot_counter = 0
        for j in range(0, len(current_words)):
            content_array_with_spaces.append(words_copy.pop(0))
            if (len(space_slots_content)>=1):
                content_array_with_spaces.append(space_slots_content.pop(0))

        plain_content = "".join(content_array_with_spaces)

        return plain_content


    last_word = False
    while(word_pointer < total_words):
        new_word_len = len(words[word_pointer])
        new_word = words[word_pointer]

        # check if there is space for a new word
        if (can_word_fit(current_words_len, new_word_len, number_of_words_in_line)):
            #('it fits')
            current_words_len += new_word_len
            number_of_words_in_line += 1
            word_pointer += 1
            current_words.append(new_word)
            # align current words in line 
            if (word_pointer >= total_words ):
                last_word = True
            result_array[result_line] = align(current_words, current_words_len, number_of_words_in_line, last_word)

        else:
            current_words = []
            current_words_len = 0
            number_of_words_in_line = 0
            result_array.append('')
            result_line += 1
        
    return result_array


#words = ["This", "is", "an", "example", "of", "text", "justification."]
#words = ["This", "is", "an"]
#maxWidth = 16

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

#words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
#maxWidth = 20



result = fullJustify(words, maxWidth)
print(result)
# Time complexity: O(n)

