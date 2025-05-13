| Feature         | `list`             | `tuple`             | `set`                     | `dict`                 |
| --------------- | ------------------ | ------------------- | ------------------------- | ---------------------- |
| **Type**        | Ordered collection | Ordered collection  | Unordered collection      | Key-value pairs        |
| **Mutable?**    | ✅ Yes              | ❌ No                | ✅ Yes                     | ✅ Yes                  |
| **Duplicates?** | ✅ Allowed          | ✅ Allowed           | ❌ Not allowed             | ❌ Keys unique          |
| **Indexed?**    | ✅ Yes (by index)   | ✅ Yes (by index)    | ❌ No                      | ✅ Yes (by key)         |
| **Syntax**      | `[1, 2, 3]`        | `(1, 2, 3)`         | `{1, 2, 3}`               | `{"a": 1, "b": 2}`     |
| **Use Case**    | General collection | Fixed data (faster) | Unique items, fast lookup | Mapping keys to values |
