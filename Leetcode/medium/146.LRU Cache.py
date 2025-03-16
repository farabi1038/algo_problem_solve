class LRUCache:

    def __init__(self, capacity: int):
        
        self.l_cache = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.l_cache:
            self.l_cache.move_to_end(key)
            return self.l_cache[key]
        return -1 
        

    def put(self, key: int, value: int) -> None:
           if key in self.l_cache:
            self.l_cache[key] = value
            self.l_cache.move_to_end(key)
           else :
                if len(self.l_cache)==self.size:
                    self.l_cache.popitem(last=False)
                    self.l_cache[key] = value
                else:
                    self.l_cache[key] = value

   

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)