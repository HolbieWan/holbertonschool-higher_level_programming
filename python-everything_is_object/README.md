# Python - Everything is object

## Baic knowledge in relatin to this project:

### What is an object

+ An object is an instance of a class that represents data and methods to interact with that data.

+ **Example:**

```python
x = "Hello"  # 'x' is an object of the class str.
```

### What is the difference between a class and an object or instance

+ A class is a blueprint, while an object (or instance) is a specific realization of that blueprint.

+ **Example:**
```python
class Dog:
    pass

my_dog = Dog() # "Dog" is the class; "my_dog" is an object.
```

### What is the difference between immutable object and mutable object

+ Immutable objects cannot be changed after creation, while mutable objects can.

+ **Example:**
```python
x = (1, 2, 3)  # Immutable tuple.
y = [1, 2, 3]  # Mutable list.
```

### What is a reference
+ A reference is a variable pointing to the memory location of an object.

+ **Example:**
```python
x = [1, 2, 3]
y = x  # 'y' references the same list as 'x'.
```

### What is an assignment

+ An assignment links a variable to an object in memory.

+ **Example:****

```python
x = 10  # 'x' is assigned the value 10.
```

### What is an alias

+ An alias is a second variable that references the same object as the first.

+ **Example:**
```python
x = [1, 2, 3]
y = x  # 'y' is an alias for 'x'.
```

### How to know if two variables are identical

+ Check their memory addresses using the id() function.

+ **Example:**
```python
x = [1, 2]
y = x
print(x is y)  # True.
```

### How to know if two variables are linked to the same object

+ Check their memory addresses using the id() function.

+ **Example:**
```python
x = [1, 2]
y = x
print(id(x) == id(y))  # True.
```

### How to display the variable identifier (which is the memory address in the CPython implementation)

+ Use the id() function.

+ **Example:**
```python
x = 42
print(id(x))  # Prints the memory address.
```

### What is mutable and immutable

+ Mutable objects can be changed after creation, while immutable objects cannot.

+ **Example:**
```python
mutable = [1, 2]  # Can change.
immutable = (1, 2)  # Cannot change.
```

### What are the built-in mutable types

+ Lists, dictionaries, sets, bytearrays, and custom objects.

+ **Example:**
```python
mutable = [1, 2, 3]
```

### What are the built-in immutable types

+ Integers, floats, strings, tuples, frozensets, and bytes.

+ **Example:**
```python
immutable = (1, 2, 3)
```

### How does Python pass variables to functions

+ Python uses pass-by-object-reference (or pass-by-value of reference).

+ **Example:**
```python
def modify_list(lst):
    lst.append(4)

x = [1, 2, 3]
modify_list(x)
print(x)  # [1, 2, 3, 4].
```