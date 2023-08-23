#!/usr/bin/python3
""" A cache class using LIFO principle."""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A cache class using LIFO principle."""

    def __init__(self):
        """Initialize a class object"""
        super().__init__()
        self.indexKeys = []

    def put(self, key, item):
        """A method that assigns the item value to the dict."""
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lifo_key = self.indexKeys.pop()
            del self.cache_data[lifo_key]
            print("DISCARD: " + lifo_key)

        if item and key:
            self.cache_data[key] = item
            self.indexKeys.append(key)

    def get(self, key):
        """return the value that is linked to the key."""
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
