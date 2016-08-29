# Force Function Arguments to be Keyword-Only

*from [PEP 3102](https://www.python.org/dev/peps/pep-3102/)*

If you are worried that use of a certain function will be prone to errors with positional arguments, you can use an `*` argument to force the following ones to be keyword-only. Note that this only works in Python 3+.

The following function will not work if called positionally:
```python
def greet_names(names, *, greeting='Hello', punctuation='!'):
	name_string = ' and '.join(names)
	full_greeting = ''.join((greeting, ' ', name_string, punctuation))
	print(full_greeting)

names = ['Alice', 'Bob']

greet_names(names)
# 'Hello Alice and Bob!'

greet_names(names, 'Howdy')
# TypeError: greet_names() takes 1 positional argument but 2 were given

greet_names(names, greeting='Howdy')
# 'Howdy Alice and Bob!'
```
