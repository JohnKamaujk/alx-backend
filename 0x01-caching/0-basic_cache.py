#!/usr/bin/python3
""" BaseCache module
"""
from base_caching import BaseCaching


class BaseCache(BaseCaching):
    """ BaseCache defines:
      - your caching system
      - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None and item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key
        """
        return self.cache_data.get(key, None)
