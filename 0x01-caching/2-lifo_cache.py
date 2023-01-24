#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache define a FIFO algorithm to use cache

      To use:
      >>> my_cache = BasicCache()
      >>> my_cache.print_cache()
      Current cache:

      >>> my_cache.put("A", "Hello")
      >>> my_cache.print_cache()
      A: Hello

      >>> print(my_cache.get("A"))
      Hello

      Ex:
      >>> print(self.cache_data)
      {A: "Hello", B: "World", C: "Holberton", D: "School"}
      >>> my_cache.put("C", "Street")
      >>> print(self.cache_data)
      {A: "Hello", B: "World", D: "School",  C: "Street"}

      >>> my_cache.put("F", "COD")
      DISCARD: C
      >>> print(self.cache_data)
      {F: "COD", B: "World", D: "School", F, "COD"}
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
            modify cache data

            Args:
                key: of the dict
                item: value of the key
        """
        if key or item is not None:
            valuecache = self.get(key)
            # Make a new
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())
                    lenlast = len(keydel) - 1
                    del self.cache_data[keydel[lenlast]]
                    print("DISCARD: {}".format(keydel[lenlast]))
            # If it's None this del the key and after update the same key
            # If it's wrong fix eliminate and ask
            else:
                del self.cache_data[key]
            # Modify value
            self.cache_data[key] = item

    def get(self, key):
        """
            modify cache data

            Args:
                key: of the dict

            Return:
                value of the key
        """

        valuecache = self.cache_data.get(key)
        return valuecache
