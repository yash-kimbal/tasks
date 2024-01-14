from functools import reduce

square = lambda x: x * 2
print(square(5))


def squareF(n):
    return n * 2


print(squareF(3))

numbers = [1, 2, 3, 4, 5]
# Map
square = list(map(lambda x: x * 2, numbers))
print(square)
# Filter
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
# Reduce
sum1 = reduce(lambda x, y: x + y, numbers)
print(sum1)


def print_arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


# Function calls with different arguments
print_arguments(1, 2, 3, name="Alice", age=25)


# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# Function calls with different arguments
greet("Alice")  # Output: Hello, Alice!
greet("Bob", greeting="Hi")  # Output: Hi, Bob!
