'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique


Examples

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.


Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

'''

import time



def canCompleteCircuit(gas, cost):
    if (sum(gas) < sum(cost)):
        return -1
    n = len(gas)

    def checkCompletion(a, b):
        tank = 0
        for i in range(0, n):
            # put gas
            tank = tank + a[i]
            # travel to next station
            tank = tank - b[i]
            if(tank < 0):
                return False
            
        return True

    loops = 0
    while (loops < n):
        if (gas[loops] == 0):
            continue
        if(checkCompletion(gas, cost)):
            # found solution
            return loops
        else:
            loops += 1
            gas.append(gas.pop(0))
            cost.append(cost.pop(0))
    return -1

#gas = [1,2,3,4,5]
#cost = [3,4,5,1,2]

#gas = [2,3,4]
#cost = [3,4,3]

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

start_time = time.time()
result = canCompleteCircuit(gas, cost)
end_time = time.time()
print(f"execution time: {end_time - start_time}")
print(result)
# This approach is O(n2)


## Aproach 2: check if journey is possible. Once we know it's possible and solution is unique, check every stop/station. 
# When for example the solution is the last element, we don't need to check the beginning of the list since it's assumed there is a solution 


def canCompleteCircuit2(gas, cost):
    sum_cost = sum(cost)
    sum_gas = sum(gas)
    if sum_cost > sum_gas:
        return -1

    current_gas = 0
    starting_index = 0

    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            current_gas = 0
            starting_index = i + 1
    return starting_index


#gas = [1,2,3,4,5]
#cost = [3,4,5,1,2]

#gas = [2,3,4]
#cost = [3,4,3]

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

start_time = time.time()
result = canCompleteCircuit2(gas, cost)
end_time = time.time()
print(f"execution time: {end_time - start_time}")
print(result)
# This approach is faster O(n)