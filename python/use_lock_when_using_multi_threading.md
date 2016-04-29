Use Lock When Using Multi-threading
===================================

**from [Effective Python](http://www.effectivepython.com/), the best Python book I've read to date**

Python has a built-in `threading` module that allows you to establish concurrency in your program. Concurrency is when a program seems to do many things at once, but is still running on a single CPU core and in a shared memory space. Contrast this with parallelism, which is when a program actually runs several things at once, on separate CPU cores, with separate memory spaces.

When assigning a series of tasks to a `Thread`, you must use the `Lock` class in order to avoid [race conditions](https://en.wikipedia.org/wiki/Race_condition) in the shared memory space. This is because the `Thread` objects will switch between each other seemingly at random during runtime, and if they are modifying the same memory space, these switches will likely lead to lost or corrupted data.

By adding a `with Lock():` statement around the list of instructions for the `Thread`, the program will be forced to complete all instructions of the current `Thread` before switching to another. Keep in mind that Python is a high-level language, so what looks like one instruction in the source code may actually be several instructions at runtime. Even if the task of each `Thread` looks simple, always use the `Lock` to be safe.

Run the following code to see an example of unsafe threading:
```python
import threading

class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(uuid, number_runs, counter):  # uuid required for threading.Thread
    for _ in range(number_runs):
        counter.increment()


def run_unsafe_threads(func, number_runs, counter):
    threads = []
    for i in range(5):
        args = (i, number_runs, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


number_runs = 100000
counter = Counter()
run_unsafe_threads(worker, number_runs, counter)

print('Expected:', 500000, 'Actual:', counter.count)
```

Now, add a `Lock`, and rejoice that your program is thread-safe.
```python
import threading

class LockingCounter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self):
        with self.lock:
            self.count += 1


def worker(uuid, number_runs, counter):  # uuid required for threading.Thread
    for _ in range(number_runs):
        counter.increment()


def run_safe_threads(func, number_runs, counter):
    threads = []
    for i in range(5):
        args = (i, number_runs, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


number_runs = 100000
counter = LockingCounter()
run_safe_threads(worker, number_runs, counter)

print('Expected:', 500000, 'Actual:', counter.count)
```
