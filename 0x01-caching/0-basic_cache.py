#!/usr/bin/python3
""" BaseCache module
"""
from base_caching import BaseCaching


class BaseCache(BaseCaching):
    """ BaseCache defines:
      - your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
