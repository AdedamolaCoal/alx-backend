#!/usr/bin/env python3
"""MRU Caching"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """Initialize self"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Remove the key to re-insert it as the most recently used
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item (last item in OrderedDict)
            most_recent, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {most_recent}")

        # Add or reinsert the key as the most recently used
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        # Move key to the end as the most recently used
        self.cache_data.move_to_end(key, last=True)
        return self.cache_data[key]
