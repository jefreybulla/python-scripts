def MinWindowSubstring(strArr):
  ## Approach: sliding window checking for substring starting. 
  # Multiple passes required chaning the size of the window from n2 to n1
    str1 = strArr[0]
    str2 = strArr[1]

    n1 = len(str1)
    n2 = len(str2)

    window_size = n2
    solution = ''

    while(window_size < n1):
        # loop to increase window size
        pointer1 = 0
        pointer2 = window_size - 1
        while pointer2 < n1:
            # loop to slide the window
            current_window = str1[pointer1:pointer2 +1]
            c_w_copy = current_window[:]
            #for i in str2 :
            match_counter = 0
            for i in str2:
                #print(f"cw = {current_window}")
                #print(f"checking for {i} in {c_w_copy}")
                # loop to check substring
                if i in c_w_copy:
                    match_counter += 1
                    if match_counter >= len(str2) :
                        #print('found solution!')
                        solution = current_window
                        return current_window
                    i_index = c_w_copy.find(i)
                    c_w_copy = c_w_copy[:i_index] + c_w_copy[i_index + 1 :]
                    #print(f"c_w_copy = {c_w_copy}")
                else:
                    break
            pointer1 +=1
            pointer2 +=1
            #print('sliding window one step ->')
        window_size += 1
        #print('increasing window size <--->')




    return strArr[0]


input = ['xyzfoeaaoabc', 'foo']

result = MinWindowSubstring(input)
print(result)

