| Action            | List Exists After? | Same Object? | Memory Impact |
| ----------------- | ------------------ | ------------ | ------------- |
| `del my_list`     | ❌ No               | ❌ No         | Frees memory  |
| `my_list.clear()` | ✅ Yes              | ✅ Yes        | Empties list  |
| `my_list = []`    | ✅ Yes              | ❌ No         | New list      |
