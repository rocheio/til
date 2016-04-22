Include Non-Python Files in a Pip Package
=========================================

**from [Hans L and Anthon](http://stackoverflow.com/a/1857436)**

When deploying files using `pip`, including those referenced in a local or private Git repo, you need to explicitly state any non-python files that you want to include in your build.

You can do this by adding the following line to your `setup()` function in `setup.py`:
```python
package_data={'': ['*file1.txt', '*file2.sh', '*file3.vbs']}
```

The empty string key tells it to include these files in any parts of this package. The `*` wildcard allows it to find these files in any sub-folders.
