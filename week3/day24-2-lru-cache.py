'''
    https://leetcode.com/problems/lru-cache
    credit: https://leetcode.com/problems/lru-cache/discuss/594885/Python-Simple-implementation-with-deque-(slow)-and-OrderedDict-(fast)
'''
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stores = OrderedDict()

    def get(self, key: int) -> int:
        val = self.stores.get(key, -1)
        if val != -1:
            self.stores.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.stores:
            self.stores.move_to_end(key)
        elif len(self.stores) == self.capacity:
            self.stores.popitem(last=False)
        self.stores[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
