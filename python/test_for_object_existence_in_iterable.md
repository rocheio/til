Test for Object Existence in an Iterable
========================================

Combining the built-in [`any`](https://docs.python.org/3/library/functions.html#any) function with [generator expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions) can make a very clean, performant test for object existence in an iterable.

The one-liner is:
```python
has_value = any(True for _ in objlist if _.attribute == 'value')
```

This will loop through any iterable of Python objects, testing each one for a desired attribute, and will return True at the first instance of any match. Because of the underlying generator expression, the test uses low memory even in very long iterables.