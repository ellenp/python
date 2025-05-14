| Feature         | `list`             | `tuple`             | `set`                     | `dict`                 |
| --------------- | ------------------ | ------------------- | ------------------------- | ---------------------- |
| **Type**        | ✅ Ordered collection | ✅ Ordered collection  | ❌ Unordered collection      | ✅ Key-value pairs        |
| **Mutable?**    | ✅ Yes              | ❌ No                | ✅ Yes                     | ✅ Yes                  |
| **Indexed?**    | ✅ Yes (by index)   | ✅ Yes (by index)    | ❌ No                      | ✅ Yes (by key)         |
| **Duplicates?** | ✅ Allowed          | ✅ Allowed           | ❌ Not allowed             | ❌ Keys unique          |
| **Syntax**      | `[1, 2, 3]`        | `(1, 2, 3)`         | `{1, 2, 3}`               | `{"a": 1, "b": 2}`     |
| **Use Case**    | General collection | Fixed data (faster) | Unique items, fast lookup | Mapping keys to values |



| Feature / Type             | `list`                   | `tuple`              | `set`                               | `dict`                          | `array.array`                | `numpy.array`                           |
| -------------------------- | ------------------------ | -------------------- | ----------------------------------- | ------------------------------- | ---------------------------- | --------------------------------------- |
| **Ordering**               | ✅ Ordered (since 3.7)      | ✅ Ordered (since 3.7)  | ❌ Unordered                           | ✅ Ordered (since 3.7)             | ✅ Ordered                      | ✅ Ordered                                 |
| **Mutability**             | ✅ Mutable                  | ❌ Immutable            | ✅ Mutable (elements must be hashable) | ✅ Mutable (keys must be hashable) | ✅ Mutable                      | ✅ Mutable                                 |
| **Indexing**               | ✅ Yes                      | ✅ Yes                  | ❌ No                                  | ✅ Keys only (not positional)      | ✅ Yes                          | ✅ Yes                                     |
| **Duplicates Allowed**     | ✅ Yes                      | ✅ Yes                  | ❌ No                                  | ❌ No, keys should be unique (values can have duplicates)         | ✅ Yes                          | ✅ Yes                                     |
| **Homogeneous Elements**   | No                       | No                   | No                                  | Keys & values can be any type   | Yes (same type only)         | Yes (same type preferred)               |
| **Memory Efficiency**      | Medium                   | High                 | High                                | Medium                          | High                         | Very High (especially for large arrays) |
| **Performance (Numerics)** | Slow                     | Slow                 | Not intended                        | Not intended                    | Faster than list             | Fastest (vectorized ops)                |
| **Used for**               | General-purpose sequence | Fixed collections    | Unique items                        | Key-value pairs                 | Numeric arrays               | Scientific computing                    |
| **Supports Comprehension** | Yes                      | Yes (via conversion) | Yes                                 | Yes                             | No                           | Yes                                     |
| **Module Required**        | No                       | No                   | No                                  | No                              | Yes (`import array`)         | Yes (`import numpy`)                    |
| **Type Constraints**       | None                     | None                 | Elements must be hashable           | Keys must be hashable           | Single type (e.g., 'i', 'f') | Single type (dtype)                     |
| **Vectorized Ops**         | No                       | No                   | No                                  | No                              | Limited                      | Yes                                     |


Additional Notes:
list: Great for general-purpose sequences, supports slicing, comprehension, and is very flexible.

tuple: Ideal for fixed collections or when immutability is required (e.g., as dict keys).

set: Useful for fast membership tests, eliminating duplicates.

dict: Core mapping type, widely used for associative arrays or hash maps.

array.array: Lightweight numeric array with less overhead than a list but less powerful than NumPy.

numpy.array: Most powerful for numerical operations, supports broadcasting, slicing, linear algebra, etc.