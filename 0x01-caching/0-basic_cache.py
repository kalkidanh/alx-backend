#!/usr/bin/python3
""" A class that is a caching system."""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A cache class that inherits from BaseCaching."""

    def put(self, key, item):
        """ A method that assigns the item value to the dict."""
        if item and key:
            self.cache_data[key] = item

    def get(self, key):
        """ A function that returns the value linked to key"""
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
