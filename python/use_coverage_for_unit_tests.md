# Use Coverage.py for Unit Test Coverage

*from [Coverage.py on readthedocs ](https://coverage.readthedocs.io/en/coverage-4.4.1/#quick-start)*

Install the `coverage` package from PyPI. Then run it against all unittests for your codebase.

```bash
$ python3.6 -m pip install coverage
$ python3.6 -m coverage run -m nose
```

Run the report, filtering files to only show those in the folders you care about.

```bash
$ python3.6 -m coverage report --include="app/*,scripts/*"
```

Remember to modify your `.gitignore` file to ignore the directories used by `coverage`.

```
.coverage
```
