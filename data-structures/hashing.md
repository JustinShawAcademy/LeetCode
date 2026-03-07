# Hashing
## Problems
- easy - [1. Two Sum](https://leetcode.com/problems/two-sum/description/)
- easy - [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) 
- medium - [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Time and Space Complexity
| Operation | HashMap | TreeMap | Array (Sorted) | Array (Unsorted) |
| :--- | :--- | :--- | :--- | :--- |
| Insert | $O(1)$ | $O(\log n)$ | $O(n)$ | $O(1)$ |
| Remove | $O(1)$ | $O(\log n)$ | $O(n)$ | $O(n)$ |
| Search | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| Inorder Traversal | $O(n \log n)$ | $O(n)$ | $O(n)$ | N/A |

## Syntax
In Python, the concepts of a HashMap and a HashSet are built directly into the language as Dictionaries and Sets.

Both are implemented using Hash Tables, meaning they offer the O(1) average time complexity for search, insert, and delete operations that you saw in your chart.

### HashMap Equivalent: `dict`
A dictionary stores data in key-value pairs.
```py
# Initialization
my_map = {}  # or dict()

# Insert or Update: O(1)
my_map["apple"] = 5
my_map["banana"] = 10

# Search (Lookup): O(1)
if "apple" in my_map:
    print(f"Price of apple: {my_map['apple']}")

# Remove: O(1)
del my_map["banana"]  # or my_map.pop("banana")

# Useful Method: .get() 
# Prevents an error if the key doesn't exist (returns None or a default value)
price = my_map.get("orange", 0)
```

### HashSet Equivalent: `set`
A set stores unique elements only. It is essentially a HashMap where you only care about the keys, not the values.

```py
# Initialization 
# Note: {} creates an empty dict, so you MUST use set() for an empty set.
my_set = set() 
my_set = {1, 2, 3} # Set literal

# Insert: O(1)
my_set.add(4)
my_set.add(1) # Duplicates are automatically ignored

# Search: O(1)
if 3 in my_set:
    print("Found 3!")

# Remove: O(1)
my_set.remove(2) # Throws error if not found
my_set.discard(99) # Does NOT throw error if not found

# Set Operations (Unique to Sets)
other_set = {3, 4, 5}
print(my_set | other_set)  # Union: {1, 3, 4, 5}
print(my_set & other_set)  # Intersection: {3, 4}
```