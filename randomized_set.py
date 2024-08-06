'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
'''


print('Approach 1')

'''
Approach 1: using sets
'''
import random
class RandomizedSet:

    def __init__(self):
        # create empty set
        self.content = set()

    def insert(self, val: int) -> bool:
        if val in self.content:
            return False
        self.content.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.content:
            self.content.remove(val)
            return True
        return False
        return True

    def getRandom(self) -> int:
        random_element = random.choice(list(self.content))
        #random_element = self.content.pop()
        #self.content.add(random_element)

        return random_element

r = RandomizedSet()
print(r)
print(r.insert(10))
print(r.insert(13))
print(r.remove(15))

print(r.content)

print(r.getRandom())



print('Approach 2')

'''
Approach 2: using lists
'''


import random
class RandomizedSet2:

    def __init__(self):
        # create empty set
        self.content = []

    def insert(self, val: int) -> bool:
        if val in self.content:
            return False
        self.content.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.content:
            self.content.remove(val)
            return True
        return False
        return True

    def getRandom(self) -> int:
        random_index = random.randrange(len(self.content)-1)
        random_element = self.content[random_index]

        return random_element

r = RandomizedSet2()
print(r)
print(r.insert(10))
print(r.insert(13))
print(r.remove(15))

print(r.content)

print(r.getRandom())

# Time execution seem similar for both approaches