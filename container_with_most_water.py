'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''



import time

'''
Aproach 1. 
For each element:
- Check every water container (area) possible to the right of the element
- Compare all areas to determined the largest area for this element. Save the max
- Compare the max area of every element and choose the max
'''

height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
start_time = time.time()

max_area = 0
for i in range(len(height)-1):
    # check areas right of the element
    max_loop_area = 0
    for j in range(i+1,len(height)):
        if height[i] > height[j]:
            bucket_height = height[j]
        else:
            bucket_height = height[i]
        bucket_width = j-i
        loop_area = bucket_height * bucket_width
        if loop_area > max_loop_area:
            max_loop_area = loop_area
    if max_loop_area > max_area:
        max_area = max_loop_area


print('max_area ->')
print(max_area)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))

'''
Aproach 2. 
For the first element:
- Check every water container (area) possible to the right of the element
- Compare all areas to determined the largest area for this element. Save the max
For all other elements
- Only if element height is larger than the element with the current max
    - run calculations. If new max, save.
    - otherwise skip
'''

#height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]

start_time = time.time()
max_area = 0
element_max_area = 0

print('Approach 2 ->>')
for i in range(len(height)-1):
    max_loop_area = 0
    if height[i] > height[element_max_area]  or i == 0:
        for j in range(i+1,len(height)):
            if height[i] > height[j]:
                bucket_height = height[j]
            else:
                bucket_height = height[i]
            bucket_width = j-i
            loop_area = bucket_height * bucket_width
            if loop_area > max_loop_area:
                max_loop_area = loop_area
        if max_loop_area > max_area:
            max_area = max_loop_area
            element_max_area = i

print('max_area ->')
print(max_area)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))
# Execuion time for large list:  ~68 seconds


'''
Aproach 3. 
For the first element:
- Check every water container (area) possible to the right of the element
- Compare all areas to determined the largest area for this element. Save the loop_max
For all other elements
- Only if element height is larger than the element with the current max AND
- if the possible loop_max_area is higher than the current max_area:
    - run calculations. If new max, save.
    - otherwise skip
'''


print('Approach 3 ->>')
height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
#height = [1,2,3,4,5,6,7,8,9,10]


#height.reverse()
#print(height)
start_time = time.time()
max_area = 0
element_max_area = 0
for i in range(len(height)-1):
#for i in range(1,2):
    max_loop_area = 0
    if height[i] > height[element_max_area]  or i == 0:
        elements_left = len(height) - i
        possible_max_area = height[i] * elements_left
        if possible_max_area > max_area:
            for j in range(i+1,len(height)):
                if height[i] > height[j]:
                    bucket_height = height[j]
                else:
                    bucket_height = height[i]
                bucket_width = j-i
                loop_area = bucket_height * bucket_width
                if loop_area > max_loop_area:
                    max_loop_area = loop_area
            if max_loop_area > max_area:
                max_area = max_loop_area
                element_max_area = i

print('max_area ->')
print(max_area)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))
# Execuion time for large list:  ~67 seconds



'''
Aproach 4. 
For the first element:
- Check every water container (area) possible to the right of the element
- Compare all areas to determined the largest area for this element. Save the loop_max
For all other elements
- Only if element height is larger than the element with the current max AND
- if the possible loop_max_area is higher than the current max_area:
    - run calculations. If new max, save.
    - otherwise skip
- For inner loop:
    - Run loop from the end to the start
    - Only run calculation for new higher heights. Otherwise skip calculation
'''


print('Approach 4 ->>')
height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
#height = [1,2,3,4,5,6,7,8,9,10]


#height.reverse()
#print(height)
start_time = time.time()
max_area = 0
element_max_area = len(height)-1
for i in range(len(height)-1):
#for i in range(1,2):
    max_loop_area = 0
    element_loop_max_area = 0
    if height[i] > height[element_max_area]  or i == 0:
        elements_left = len(height) - i
        possible_max_area = height[i] * elements_left
        if possible_max_area > max_area:
            #print('--> i')
            #print(i)
            for j in range(len(height)-1,i+1,-1):
                if j == len(height)-1 or height[j] > height[element_loop_max_area]:
                    #print('j ->')
                    #print(j)
                    if height[i] > height[j]:
                        bucket_height = height[j]
                    else:
                        bucket_height = height[i]
                    bucket_width = j-i
                    loop_area = bucket_height * bucket_width
                    if loop_area > max_loop_area:
                        max_loop_area = loop_area
                        element_loop_max_area = j
            if max_loop_area > max_area:
                max_area = max_loop_area
                element_max_area = i

print('max_area ->')
print(max_area)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))
# Execuion time for large list:  ~102 seconds


'''
Aproach 5. 
Have two pointers: one starting at 0, the other sarting at the end of the list
Calculate area on each step and keep track of max_area
Move pointer with the lowest heigh value
End when both pointers are next to each other. Return max_area
'''



print('Approach 5 ->>')
#height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
#height = [1,2]
#height=[1,2,4,3]
#height = [1,2,3,4,5,6,7,8,9,10]



start_time = time.time()
pointer_left = 0
pointer_right = len(height)-1
max_area = 0

while True:
    bucket_width = pointer_right - pointer_left
    bucket_height = min(height[pointer_left], height[pointer_right])
    loop_max_area = bucket_width * bucket_height
    if loop_max_area > max_area:
        max_area = loop_max_area
    if pointer_left == pointer_right -1:
        break
    if height[pointer_left] <= height[pointer_right]:
        pointer_left = pointer_left + 1
    else:
        pointer_right = pointer_right - 1

print (max_area)
end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))
# Execuion time for large list: 0.016910076141357422 s !!!
