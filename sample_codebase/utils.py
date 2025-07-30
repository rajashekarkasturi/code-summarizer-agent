# A simple in-memory cache with a fixed capacity.

import time

class SimpleCache:
    """
    A basic key-value cache that stores a limited number of items.
    When the cache is full, it does not add new items.
    """
    def __init__(self, capacity: int = 10):
        """
        Initializes the cache with a specific capacity.
        
        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self._cache = {}
        self._timestamps = {}

    def get(self, key: str) -> object:
        """
        Retrieves an item from the cache.
        
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self._cache.get(key)

    def set(self, key: str, value: object) -> bool:
        """
        Adds a key-value pair to the cache.
        If the cache is full and the key is new, the operation will fail.
        
        Returns:
            True if the item was set successfully, False otherwise.
        """
        if key not in self._cache and len(self._cache) >= self.capacity:
            print(f"Warning: Cache is full. Cannot set key '{key}'.")
            return False
            
        self._cache[key] = value
        self._timestamps[key] = time.time()
        return True

    def clear(self):
        """Removes all items from the cache."""
        self._cache.clear()
        self._timestamps.clear()
        print("Cache has been cleared.")