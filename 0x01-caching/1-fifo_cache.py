#!/usr/bin/env python3
""" FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                else:
                    least_used = min(self.cache_data, key=self.cache_data.get)
                    del self.cache_data[least_used]
            self.cache_data[key] = item
