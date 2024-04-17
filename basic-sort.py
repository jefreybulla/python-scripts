import time

numbers = [10,9,8,7,6,5,4,3,2,1]

print("Original list: ", numbers)

start_time = time.time()
print(start_time)
# sort list algorithm 
for i in range(len(numbers)):
    postive_comparison = 0
    for i in range(len(numbers)-1):
        print('index-->')
        print(i)
        print (numbers[i])
        #break

        if numbers[i] < numbers[i+1]:
            print('nothin to do')
            postive_comparison = postive_comparison + 1
        else:
            number_big = numbers[i]
            number_small = numbers[i+1]
            numbers[i] = number_small
            numbers[i+1] = number_big
    if postive_comparison >= len(numbers)-1:
        break

print(numbers)

end_time = time.time()
print("--- %s seconds ---" %(end_time - start_time))

# Algorith time complexity is Big O(n^2) since it needs to execute n times n in the worse case