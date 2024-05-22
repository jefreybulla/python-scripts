'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 Examples

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''


print('Approach 1')

'''
Approach 1:
1. Use two pointers: pointer1 keep track of current position. Pointer 2 tracks the farthest elements I can reach
2. Jump the max steps and ask: was the end reach?
3. If yes, return true
4. If no, move pointer1 one position. Check that pointer 1 <= pointer 2. Otherwhise return false
'''

def jump_game(nums):
    pointer1 = 0
    pointer2 = 0
    nums_length = len(nums)
    if nums_length == 1:
        return True
    while True:
        print(f"pointer1 {pointer1}") 
        if nums[pointer1] == 0 and pointer1 < pointer2:
            pointer1 += 1
            continue
        if pointer1 + nums[pointer1] > pointer2:
            pointer2 = pointer1 + nums[pointer1]
        if pointer1 >= pointer2:
            return False
        if pointer2 >= nums_length - 1:
            return True
        else:
            pointer1 += 1



#nums = [2,3,1]
#nums = [2,3,1,1]
#nums = [3,2,1,0,4] # false
#nums = [2,5,0,0]
#nums = [0,1]
#nums = [0]
#nums = [3,0,8,2,0,0,1] #true
#nums = [3,2,1,0,4] #false
nums = [5,9,3,2,1,0,2,3,3,1,0,0] # true
result = jump_game(nums)
print(result)



'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 
Examples

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
'''


print('## Jump game 2')

def jump_game_2(nums):
    nums_length = len(nums)
    if nums_length == 1:
        return 0
    pointer1 = 0
    pointer2 = pointer1 + nums[pointer1]
    number_of_jumps = 1
    
    farthest_jump = 0
    while pointer2 < nums_length -1:
        #print(f"pointer1 {pointer1}")
        #print(f"pointer2 {pointer2}")
        for i in range(pointer1, pointer2 + 1):
            local_jump = nums[i] + i
            if local_jump > farthest_jump:
                farthest_jump = local_jump
                new_pointer1 = i
        pointer1 = new_pointer1
        pointer2 = farthest_jump
        number_of_jumps += 1
    return number_of_jumps

#nums = [2,3,1,1,4]
#nums = [2,3,0,1,4]
#nums = [0]
#nums = [1,2,1,1,1]
nums = [1,2,3]
#nums = [2,0,2,0,1]
#nums = [5,9,3,2,1,0,2,3,3,1,0,0]    #3

#nums = [2,1]

result = jump_game_2(nums)
print(result)