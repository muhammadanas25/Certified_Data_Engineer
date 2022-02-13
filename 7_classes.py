# Creating and Using a Class

# Let’s start by writing a simple class, Dog, that represents a dog—not one dog in particular, 
# but any dog. What do we know about most pet dogs? Well, they all have a name and age. 
# We also know that most dogs sit and roll over. Those two pieces of information (name and age) 
# and those two behaviors (sit and roll over) will go in our Dog class because they’re common to most dogs. 
# This class will tell Python how to make an object representing a dog. After our class is written, 
# we’ll use it to make individual instances, each of which represents one specific dog.

class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command.""" 
        print(f"{self.name} rolled over!")

# Making an Instance from a Class

dog_instance = Dog(name='tom',age=3)
dog_instance.roll_over()

# 11. we write a docstring describing what this class does.
# 12. The __init__() method is a special method that Python runs automatically whenever we create a new instance based
    # on the Dog class. This method has two leading underscores and two trail- ing underscores, a convention that helps 
    # prevent Python’s default method names from conflicting with your method names.
# 14. The two variables defined each have the prefix self. Any variable prefixed with self is available to every method in the class 
    # and we’ll also be able to access these variables through any instance created from the class.
# The Dog class has two other methods defined: sit() and roll_over().

# Accessing Attributes
# To access the attributes of an instance, you use dot notation. we access the value of my_dog’s attribute name by writing:
dog_instance.name


# Calling Methods
dog_instance.roll_over()
dog_instance.sit()

# Creating Multiple Instances

# You can create as many instances from a class as you need. Let’s create a second dog called your_dog:
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.") 
print(f"My dog is {my_dog.age} years old.") 
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# more examples
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year=2015): 
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model 
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4')
print(my_new_car.get_descriptive_name())


# Importing a Module into a Module

# from modules.car import Car
from modules.car import Car
# Using Aliases

from modules.car import Car 

