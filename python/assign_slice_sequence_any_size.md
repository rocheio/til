Assign a List Slice to a Sequence of Any Size
=============================================

*from [Effective Python, Page 12](http://www.effectivepython.com/)*

Unlike tuple assignments, which are immutable, a slice of a list can be assigned to another sequence of any size. The original list will be modified in-place, and will shrink or expand to fit all of the new values.

```python
some_list = [1, 2, 3, 4, 5, 6, 7]
some_list[1:-1] = [8, 9]
print(some_list)  # [1, 8, 9, 7]
```