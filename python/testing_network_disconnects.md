# Testing Network Disconnects

*from [Thomas Orozco on Stack Overflow](https://stackoverflow.com/questions/18601828/python-block-network-connections-for-testing-purposes/18601897#18601897)*

Monkey-patch the `socket` module to mimic a network error when a connection is attempted.

```python
class NetworkTestError(Exception):
    pass

def disable_network():
    import socket
    def guard(*args, **kwargs):
        raise NetworkTestError
    socket.socket = guard
```

Use a custom `Exception` class so that you can catch it when testing the control case.

```python
disable_network()

with self.assertRaises(NetworkTestError):
    unsafe_function()

response = safe_function()
assert response.error_code = 400  # or whatever...
```
