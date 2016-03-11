Access Help and Documentation in the Terminal
=============================================

There's nothing wrong with searching [StackOverflow](http://stackoverflow.com/) for help, but it can be quicker to access the documentation of the code in question directly. This is especially useful when you do not have access to the internet.

In any instance of Python, the built-in [`help()`](https://docs.python.org/3/library/functions.html#help) function will display detailed documentation about any Python module or function that has a docstring. 

Open the terminal and type `python -i` to use the default Python interactive, or `ipython` to use the IPython interactive (preferred). Usage is straightforward:

```python
import passlib
help(passlib)
```

If the top-level documentation is not enough, explore the module further using the [`dir()`](https://docs.python.org/3/library/functions.html#dir) function, then call `help()` on any relevant sub-modules or functions. If calling `help()` returns `TypeError: 'NoneType' object is not iterable`, then there is no documentation available for that object, and you'll need to explore the documentation of parent/sibling/child objects.

```python
dir(passlib)
import passlib.hash
help(passlib.hash)
dir(passlib.hash)
from passlib.hash import sha256_crypt
help(sha256_crypt)  # TypeError because no docstring exists at this level
dir(sha256_crypt)
help(sha256_crypt.encrypt)
```

IPython offers even more tools for documentation access in the terminal. In addition to making all of the above commands print in a more readable fashion (e.g. printing lists with one item per line), it offers it's own `?` and `??` syntax to access documentation. If the built-in `help()` function does not provide enough info, it's often worthwhile to check the IPython documentation as well before tabbing over to the browser.

```python
from passlib.hash import sha256_crypt
help(sha256_crypt.encrypt)  # Python built-in help syntax
sha256_crypt.encrypt?  # IPython-specific help summary
sha256_crypt.encrypt??  # IPython-specific help detail
```
