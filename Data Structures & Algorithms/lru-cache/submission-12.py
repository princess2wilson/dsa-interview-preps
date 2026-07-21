from collections import defaultdict, OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.order = OrderedDict()
        self.hashmap = defaultdict(int)
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.order.move_to_end(key,last = False)
            return self.hashmap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        self.order[key] = value
        self.order.move_to_end(key,last = False)

        if len(self.hashmap)>self.capacity:
            key,value = self.order.popitem(last=True)
            del self.hashmap[key]

