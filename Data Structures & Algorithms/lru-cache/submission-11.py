from collections import defaultdict,OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.order:
            self.order.move_to_end(key)
            return self.order[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key not in self.order:
            if len(self.order) >= self.capacity:
                lfu,index = self.order.popitem(last = False)
        self.order[key] = value
        self.order.move_to_end(key)

        
