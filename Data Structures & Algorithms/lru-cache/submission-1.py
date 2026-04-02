from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.data_store = {}
        self.data_order = deque()
        

    def get(self, key: int) -> int:
        if key in self.data_store:
            self.data_order.remove(key)
            self.data_order.append(key)
            return self.data_store[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.data_store:
            self.data_order.remove(key)
        elif len(self.data_store) == self.capacity:
            self.data_store.pop(self.data_order.popleft())
            
        self.data_store[key] = value
        self.data_order.append(key)