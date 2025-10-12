# | Operation                    | Example            | Reason                                                                                                    |
# | ---------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------- |
# | **Modify elements directly** | `s[0] = 'H'`       | Strings are **immutable**, so you cannot change a character in-place. Any change creates a new string.    |
# | **append()**                 | `s.append('!')`    | Strings do not support adding elements in-place like lists; you must concatenate a new string instead.    |
# | **extend()**                 | `s.extend('abc')`  | No method to extend a string in-place; use concatenation instead: `s = s + 'abc'`.                        |
# | **insert()**                 | `s.insert(1, 'x')` | Cannot insert at a specific position in a string; strings cannot be changed in-place.                     |
# | **remove()**                 | `s.remove('h')`    | Strings do not support removal of elements; you need to create a new string using slicing or `replace()`. |
# | **pop()**                    | `s.pop()`          | No concept of “popping” a character from a string. Use slicing or convert to a list first.                |
# | **clear()**                  | `s.clear()`        | Strings do not have a `clear()` method; to empty a string, assign `s = ''`.                               |
# | **sort()**                   | `s.sort()`         | Strings cannot be sorted in-place; you can create a sorted version using `''.join(sorted(s))`.            |
# | **reverse()**                | `s.reverse()`      | Strings cannot be reversed in-place; you can create a reversed version using slicing: `s[::-1]`.          |
