#!/usr/bin/env python3
"""LFU Caching"""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
            self.usage_frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k, v in self.usage_frequency.items() if v == min_freq]

                # Among LFU items, remove the least recently used
                if lfu_keys:
                    lfu_key = lfu_keys[0]
                    for k in lfu_keys:
                        if k in self.cache_data:
                            lfu_key = k
                            break
                    self.cache_data.pop(lfu_key)
                    del self.usage_frequency[lfu_key]
                    print(f"DISCARD: {lfu_key}")

            # Insert the new item with frequency 1
            self.usage_frequency[key] = 1
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieve an item by key"""
        if key is not None and key in self.cache_data:
            self.usage_frequency[key] += 1
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
