# AuthTokenCache

A simple Python implementation of an in-memory cache for authentication tokens. This class is designed to reduce the latency introduced by frequent requests to a third-party authentication service by caching tokens locally. The cache has a fixed size and uses a First-In-First-Out (FIFO) eviction strategy when the cache reaches its capacity.

## Features

- **In-Memory Caching**: Tokens are stored in an in-memory `OrderedDict`, ensuring fast access and low latency.
- **FIFO Eviction**: When the cache is full, the oldest token is removed to make space for new ones.
- **Easy Integration**: The `AuthTokenCache` class can be easily integrated into any Python project that interacts with external authentication services.

## Installation

To use the `AuthTokenCache` class, simply clone this repository or copy the class definition into your project.

```bash
git clone https://github.com/aminakm123/auth-token-cache.git
