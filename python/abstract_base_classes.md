Use Abstract Base Classes to Enforce Structure
==============================================

Python has a built-in [`abc`](https://docs.python.org/3/library/abc.html) module that makes it easy to enforce standard class structures in a project.

Instead of writing extensive documentation and attempting to enforce structure through policy, the `abc` module enforces this structure programatically, and makes it easy to require all subclasses to include certain methods or attributes, even if the details of those methods are not known ahead of time or vary in implementation.

For example, imagine a class for an autonomous car with a method that makes the car drive to its owner's current location. You hire some new developers to help you design other autonomous vehicles, and want to have a `go_to_owner` method that is standard across all of them.

First, create an `AutonomousVehicle` class to serve as the abstract base class.

```python
import abc

class AutonomousVehicle(metaclass=abc.ABCMeta):
    def __init__(self):
        print('New vehicle instantiated')

    @abc.abstractmethod
    def go_to_owner(self):
        """Make the vehicle go to its owner's current location."""
        pass
```

Now that the base class is defined, create an `AutonomousCar` subclass from it. Note that the `AutonomousVehicle` class *cannot* be instantiated directly- it's just a blueprint for other classes.

```python
class AutonomousCar(AutonomousVehicle):
    def go_to_owner(self):
        print('Now driving to owner')

car = AutonomousCar()
car.go_to_owner()
```

The system works! Now imagine a new developer, working on the `AutonomousPlane` class, tries to subclass without this method.

```python
class AutonomousPlane(AutonomousVehicle):
    def fly(self):
        print('Just flying around')

plane = AutonomousPlane()
plane.fly()
```

This script will fail at class definition, returning `TypeError: Can't instantiate abstract class AutonomousPlane with abstract methods go_to_owner`. This lets the developer know that they must build that method before their work is complete.

The `abc` module is certainly not foolproof, but its a great way to enforce a standard class structure and keep an object-oriented codebase in sync.