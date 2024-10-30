#!/usr/bin/env python3
"""LRU Caching"""

from collections import OrderedDict
from functools import lru_cache
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """initialize self"""
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
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """to remove the least used item"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        """returns the get value for the key"""
        return self.cache_data.get(key, None)
