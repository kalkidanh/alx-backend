#!/usr/bin/python3
""" A cache class using the MRU method."""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ A caching class that uses the MRU method."""

    def __init__(self):
        """ Initializes the object."""
        super().__init__()
        self.indexKeys = []

    def put(self, key, item):
        """ Method that assigsn the item value to the dict."""
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.indexKeys.pop(0)
            del self.cache_data[mru_key]
            print("DISCARD: " + mru_key)

        if item and key:
            if key in self.indexKeys:
                self.indexKeys.remove(key)
            self.cache_data[key] = item
            self.indexKeys.insert(0, key)

    def get(self, key):
        """return the value that is linked to key."""
        if key not in self.cache_data.keys():
            return None
        self.indexKeys.remove(key)
        self.indexKeys.insert(0, key)
        return self.cache_data[key]
