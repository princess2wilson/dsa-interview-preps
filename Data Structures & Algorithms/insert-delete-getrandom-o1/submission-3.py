import random
from collections import Counter
class RandomizedSet:

    def __init__(self):
        self.random_set = []
        self.my_set = {}

    def insert(self, val: int) -> bool:
        if val in self.my_set:
            return False
        self.random_set.append(val)
        self.my_set[val] = len(self.random_set)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.my_set:
            return False
        temp = self.random_set[-1]
        index = self.my_set[val]
        self.random_set[-1] = val
        self.random_set[index] = temp
        self.my_set[temp] = index
        self.random_set.pop()
        self.my_set.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.random_set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()