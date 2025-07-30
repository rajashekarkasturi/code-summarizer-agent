# AI-Generated Codebase Summary

## File: `sample_codebase\data_analyzer.py`

### Function: `analyze_sales_data`

**Description:**
Analyzes a list of sales records to compute total revenue, total items sold, and the best-selling product.

**Parameters:**
- `records` (list[dict]): A list of sales records, each containing 'product_id', 'quantity', and 'price' keys.

**Returns:**
dict with keys 'total_revenue' (float), 'total_items_sold' (int), and 'best_selling_product' (str or None).

**Usage Example:**
```python
result = analyze_sales_data([
    {'product_id': 'A123', 'quantity': 2, 'price': 19.99},
    {'product_id': 'B456', 'quantity': 5, 'price': 9.99}
])
print(result)  # {'total_revenue': 89.93, 'total_items_sold': 7, 'best_selling_product': 'B456'}
```

---

## File: `sample_codebase\utils.py`

### Class: `SimpleCache`

**Overall Description:**
SimpleCache is a lightweight, in-memory key-value cache that enforces a strict upper bound on the number of stored items. When the cache reaches its capacity, any attempt to add a new key is rejected rather than evicting existing entries. It provides basic operations for retrieval, insertion, and clearing of cached data.

**Initialization:**
The constructor accepts a single optional parameter, `capacity`, which determines the maximum number of key-value pairs the cache can hold (default is 10). Internally, it initializes two dictionaries: `_cache` for storing the actual data and `_timestamps` for tracking insertion times.

**Key Methods:**
- `get(key: str) -> object` – Returns the value associated with `key` if it exists, otherwise returns `None`.
- `set(key: str, value: object) -> bool` – Stores `value` under `key`. Returns `True` on success; if the cache is full and the key is new, it prints a warning and returns `False`.
- `clear()` – Removes every entry from the cache and resets the timestamp dictionary, then prints a confirmation message.

**Usage Example:**
```python
from simple_cache import SimpleCache

# Create a cache that can hold up to 3 items
cache = SimpleCache(capacity=3)

# Add items
cache.set('a', 1)
cache.set('b', 2)
cache.set('c', 3)

# Attempt to add a fourth item (will fail)
cache.set('d', 4)  # prints: Warning: Cache is full. Cannot set key 'd'.

# Retrieve an item
print(cache.get('b'))  # outputs: 2

# Clear the cache
cache.clear()  # prints: Cache has been cleared.
```

---

