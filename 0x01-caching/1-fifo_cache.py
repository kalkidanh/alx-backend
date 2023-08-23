#!/usr/bin/python3
""" A cache class using FIFO."""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A caching class that uses FIFO principle."""

    def __init__(self):
        """ Initializes the object."""
        super().__init__()
        self.indexKeys = []

    def put(self, key, item):
        """ A method that assigns the item value to the dict."""
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            fifo_key = self.indexKeys.pop(0)
            del self.cache_data[fifo_key]
            print("DISCARD: " + fifo_key)

        if item and key:
            self.indexKeys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to the key."""
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
