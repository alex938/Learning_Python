import time
from functools import lru_cache

def fibonacci_no_cache(n):
    if n < 2:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

@lru_cache(maxsize=None)  #maxsize=None means the cache can grow indefinitely
def fibonacci_with_cache(n):
    if n < 2:
        return n
    return fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)

start_time_no_cache = time.time()
fibonacci_no_cache(30)  
end_time_no_cache = time.time()
no_cache_duration = end_time_no_cache - start_time_no_cache

start_time_with_cache = time.time()
fibonacci_with_cache(30)
end_time_with_cache = time.time()
with_cache_duration = end_time_with_cache - start_time_with_cache

print(f"Execution time without cache: {no_cache_duration:.6f} seconds")
print(f"Execution time with cache: {with_cache_duration:.6f} seconds")
