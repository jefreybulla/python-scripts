import time

numbers = [10,9,3,7,5,6,4,8,2,1]

print("Original list: ", numbers)

start_time = time.time()
print(start_time)
# Bubble sort algorithm with stop optimization
for i in range(len(numbers)):
    postive_comparison = 0
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
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


print('using sorted')
start_time = time.time()
print(sorted(numbers))
end_time = time.time()

print("--- %s seconds ---" %(end_time - start_time))

# My algorigthm seems to run a bit faster than python's sorted