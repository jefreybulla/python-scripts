'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Examples:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

'''

## Approach: Pointer1 is a local_top. Move right from pointer1 until an elevation is >= local_top. 
# Water are is equal to ((local_top * wide) - each element in between ) 
# Run this algo twice: once from left to right, once right lo left.
# Use water_found_array to track water already added to it does not get counted twice


def trap(height):
    pointer1 = 0
    pointer1_height = 0
    area_to_substract = 0
    trap_width = 0
    water_trapped = 0
    n = len(height)
    possible_water_found_array = [0] * n
    water_found_array = [0] * n
    for i in range(0,n):
        if (height[i] >= pointer1_height ):
            water_found = (pointer1_height * trap_width) - area_to_substract
            water_trapped += water_found
            water_found_array = possible_water_found_array.copy()
            pointer1 = i
            pointer1_height = height[i]
            trap_width = 0
            area_to_substract = 0
        else:
            area_to_substract += height[i]
            trap_width += 1
            possible_water_found_array[i] = 1
            #water_found_array[i] = 1

    pointer1 = 0
    pointer1_height = 0
    area_to_substract = 0
    trap_width = 0

    for i in range(n-1,-1,-1):
        if(water_found_array[i] != 0):
            continue
        if (height[i] >= pointer1_height ):
            water_trapped += (pointer1_height * trap_width) - area_to_substract
            # keep track of water recorded so it does not get counted twice
            #water_found_array[i] = 1
            pointer1 = i
            pointer1_height = height[i]
            trap_width = 0
            area_to_substract = 0
        else:
            area_to_substract += height[i]
            trap_width += 1
    return water_trapped


#height = [4,2,0,3,2,5]     #9
height = [0,1,0,2,1,0,1,3,2,1,2,1]  #6
# reverse
#height = [1, 2, 1, 2, 3, 1, 0, 1, 2, 0, 1, 0]
#height = [0,1,0,2]
#height = [2,1,0,1,3]
#height = [3,2,1,2]
#height = [2,1,2]
#height = [2,0,2]   # 2
#height = [4,2,3]    # 1
result = trap(height)
print(result)
# Time complexity O(n)
