from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # move to end of the dict/ cache... most recently used.
            return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            # The pairs are removed in LIFO order if last = true or FIFO order if false.
            self.cache.popitem(last=False)


if __name__ == "__main__":
    l_cache = LRUCache(5)
    print(l_cache.cache)
    l_cache.put(1, 1)
    print(l_cache.cache)
    l_cache.put(2, 2)
    print(l_cache.cache)
    l_cache.put(3, 3)
    print(l_cache.cache)
    l_cache.get(2)
    print(l_cache.cache)
    l_cache.get(3)
    print(l_cache.cache)

