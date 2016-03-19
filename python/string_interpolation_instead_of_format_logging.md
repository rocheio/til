Use String Interpolation Instead of Format in Logging
=====================================================

**from [sthenault](http://stackoverflow.com/a/34634301)**

In Python, the `format` method of a string is executed immediately, regardless of the call to the logger. In contrast, the `%s` *interpolation* syntax will only be executed if it is displayed somewhere.

So, when passing arguments to a string during a step in logging (which should be most of the time), do it like this:
```python
logger.info('dataframe loaded with %s rows and %s columns',
            df.shape[0], df.shape[1])
```
