#!/usr/bin/env python3
""" FIFO caching module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        self.cache_data[key] = item
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # this is called tuple unpacking _
            least_used, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {least_used}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key, None)


# least_used = min(self.cache_data, key=self.cache_data.get)
# del self.cache_data[least_used]
