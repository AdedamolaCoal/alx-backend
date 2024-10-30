#!/usr/bin/env python3
""" FIFO caching module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # this is called tuple unpacking _
                least_used, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {least_used}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """returns the get value for the key"""
        return self.cache_data.get(key, None)
