Modify the \__init__ Method of a Python Subclass
===============================================

**from [delnan](http://stackoverflow.com/a/5636694)**

When deriving a subclass from a superclass, there will likely be a case when you want to modify or add elements to the `__init__` method of the original. To do that, you just need to use the  [`super`](https://docs.python.org/3.5/library/functions.html#super) function in the `__init__` of the subclass to call the `__init__` of the superclass.

```python
class SubClass(SuperClass):
    def __init__(self, x, y):
        super(SubClass, self).__init__(x)
        self.y = y
```
