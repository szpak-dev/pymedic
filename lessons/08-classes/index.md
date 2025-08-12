# Lesson 8: Classes

## 1. Introduction

Classes are blueprints for creating objects. They define the structure (attributes) and behavior (methods) that objects of that class will have. In Python, classes are first-class citizens, meaning they can be passed as arguments, stored in variables, and even created dynamically at runtime.

**Basic Syntax:**

```python
class Car:
    brand: str
    model: str

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def drive(self) -> None:
        print(f"The {self.brand} {self.model} is driving.")
```

**Example Usage:**

```python
car = Car("Tesla", "Model S")
car.drive()
```

*Interesting fact:* You can dynamically add attributes to objects at runtime, though this is generally discouraged for maintainability.

## 2. Attributes and Methods

Attributes are variables that belong to an object. Methods are functions defined in a class. Python supports three main kinds of methods:

* **Instance methods**: The most common. They take `self` as the first argument, giving access to the instance's attributes and other methods.
* **Class methods**: Declared with `@classmethod` and take `cls` as the first parameter, allowing access to the class itself rather than an instance. They are useful for alternative constructors or class-wide operations.
* **Static methods**: Declared with `@staticmethod` and take neither `self` nor `cls`. They behave like normal functions but live inside the class namespace for logical grouping.

**Example:**

```python
class Book:
    title: str
    author: str
    pages: int
    book_count: int = 0

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        Book.book_count += 1

    def description(self) -> str:  # Instance method
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    @classmethod
    def total_books(cls) -> int:  # Class method
        return cls.book_count

    @staticmethod
    def is_lengthy(pages: int) -> bool:  # Static method
        return pages > 300
```

```python
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)
print(book1.description())
print(Book.total_books())
print(Book.is_lengthy(500))
```

*Interesting fact:* Static methods are often used for utility functions related to a class but that don’t need instance or class-level data.

## 3. Class vs Instance Attributes

* **Instance attributes**: Belong to specific objects.
* **Class attributes**: Shared across all instances.

**Example:**

```python
class Dog:
    species: str = "Canis familiaris"

    def __init__(self, name: str) -> None:
        self.name = name
```

```python
d1 = Dog("Rex")
d2 = Dog("Buddy")
print(d1.species, d2.species)
```

*Interesting fact:* Modifying a class attribute affects all instances unless it’s shadowed by an instance attribute.

## 4. Inheritance

Inheritance allows creating a class based on another class.

**Example:**

```python
class Animal:
    def speak(self) -> str:
        return "Some sound"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

cat = Cat()
print(cat.speak())
```

*Interesting fact:* Python supports multiple inheritance, and the method resolution order (MRO) determines which base class method is used.

## 5. Polymorphism

Different classes can define methods with the same name, and Python can call them interchangeably.

**Example:**

```python
class Bird:
    def sound(self) -> str:
        return "Chirp"

class Cow:
    def sound(self) -> str:
        return "Moo"

def make_sound(animal: object) -> None:
    print(animal.sound())

make_sound(Bird())
make_sound(Cow())
```

*Interesting fact:* Python relies on duck typing — if an object implements the expected method, it can be used without explicit inheritance.

## 6. Encapsulation

Encapsulation hides internal details and controls access.

**Example:**

```python
class BankAccount:
    __balance: float

    def __init__(self, initial_balance: float) -> None:
        self.__balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance
```

*Interesting fact:* Private variables in Python are name-mangled, but not truly inaccessible.

## 7. Special Methods (Magic Methods)

Magic methods define how objects interact with built-in operations. In the `Vector` example:

* `__init__`: Constructor method called when creating an object.
* `__add__`: Defines behavior for the `+` operator.
* `__repr__`: Returns a string representation of the object, useful for debugging.

**Example:**

```python
class Vector:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
```

```python
v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)
```

*Interesting fact:* Implementing `__iter__` allows objects to be looped over directly, while `__eq__` can define equality comparison between objects.

## 8. Abstract Classes

Abstract classes define an interface without full implementation.

**Example:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2
```

```python
circle = Circle(5)
print(circle.area())
```

*Interesting fact:* Abstract classes can enforce method implementation across large codebases.


## Homework

### Banking Simulation

**Goal:** Implement different types of bank accounts with clear withdrawal and deposit rules.

**Requirements:**

* Create an abstract class `Account` with:

  * `deposit(amount: float)` method.
  * `withdraw(amount: float)` method.
  * Protected attribute `_balance`.
* Implement `SavingsAccount`:

  * Allows deposits and withdrawals.
  * Withdrawals should not exceed the balance.
  * Optional interest calculation method.
* Implement `CheckingAccount`:

  * Allows overdraft up to a certain limit.
  * Withdrawals beyond the limit should raise an exception.
* Write test cases simulating deposits, withdrawals, and overdrafts.

**Learning points:**

* Abstract classes to enforce interface.
* Encapsulation for protecting balance.
* Method overriding for different withdrawal rules.


### Geometry Toolkit

**Goal:** Create a set of geometric shapes with the ability to compare them by area.

**Requirements:**

* Create an abstract class `Shape` with:

  * `area()` method.
  * `perimeter()` method.
* Implement `Rectangle`, `Triangle`, and `Circle`:

  * Use correct geometric formulas.
* Implement magic methods:

  * `__lt__` for less-than comparison based on area.
  * `__repr__` for a readable shape description.
* Store shapes in a list and sort them by area.

**Learning points:**

* Polymorphism through the `Shape` base class.
* Magic methods for comparison and representation.
* Using sorted lists with custom object behavior.


### Video Game Characters

**Goal:** Simulate a battle system between characters with unique abilities.

**Requirements:**

* Create a base class `Character` with:

  * Attributes: `name`, `health`, `attack_power`.
  * Method `attack(target: Character)`.
* Subclasses:

  * `Warrior`: Strong melee attacks.
  * `Mage`: Magic attacks that can ignore some defense.
  * `Archer`: Ranged attacks with critical hit chance.
* Add special abilities or passive traits.
* Simulate a battle loop until one character wins.

**Learning points:**

* Inheritance for character types.
* Method overriding for unique abilities.
* Object interactions and game simulation logic.
