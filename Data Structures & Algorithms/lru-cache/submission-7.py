from collections import OrderedDict
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
        self.order[key] = value
        self.order.move_to_end(key)
        if len(self.order) > self.capacity:
            self.order.popitem(last = False)
            
