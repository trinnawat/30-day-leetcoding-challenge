'''
    https://leetcode.com/problems/lru-cache
'''
from collections import defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_list = []
        self.stores = defaultdict(int)

    def get(self, key: int) -> int:
        val = self.stores.get(key, -1)
        if val != -1:
            self.key_list.remove(key)
            self.key_list.append(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.stores:
            self.stores[key] = value
            self.get(key)
        else:
            if len(self.key_list) == self.capacity:
                lru_key = self.key_list.pop(0)
                self.stores.pop(lru_key)
            self.key_list.append(key)
            self.stores[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
