# Use Keyring to Store Sensitive Information

*from [keyring on PyPI](https://pypi.python.org/pypi/keyring#using-keyring)*

To store data securely, on a per-user basis, use the OS-level keyring service via [`keyring`](https://pypi.python.org/pypi/keyring#using-keyring).

```bash
pip install keyring
```

Using the library in practice is dead simple:

```python
import keyring
keyring.set_password('system', 'key', 'password')
password = keyring.get_password('system', 'key')
```
