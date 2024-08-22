from collections import OrderedDict

class AuthTokenCache:
    def __init__(self, max_size: int):
        """
        Initialize the token cache with a maximum size.
        :param max_size: Maximum number of tokens the cache can hold.
        """
        self.cache = OrderedDict()
        self.max_size = max_size

    def get_token(self, key: str):
        """
        Fetch a token from the cache.
        :param key: The key for the token to retrieve.
        :return: The token if it exists in the cache, or None if it doesn't.
        """
        if key in self.cache:
            # Move the accessed token to the end to mark it as recently used.
            token = self.cache.pop(key)
            self.cache[key] = token
            return token
        return None

    def set_token(self, key: str, token: str):
        """
        Add a new token to the cache.
        :param key: The key for the token.
        :param token: The token to add to the cache.
        """
        if key in self.cache:
            # If the key already exists, remove it first to update its position.
            self.cache.pop(key)
        elif len(self.cache) >= self.max_size:
            # If the cache is full, remove the oldest item (FIFO eviction).
            self.cache.popitem(last=False)
        
        # Add the new token to the cache.
        self.cache[key] = token


cache = AuthTokenCache(max_size=5)
cache.set_token("user1", "token1")
cache.set_token("user2", "token2")
cache.set_token("user3", "token3")
print(cache.get_token("user1"))  # Output: token1
cache.set_token("user4", "token4")
cache.set_token("user5", "token5")
cache.set_token("user6", "token6")
print(cache.get_token("user2"))  # Output: None, since it was evicted.
