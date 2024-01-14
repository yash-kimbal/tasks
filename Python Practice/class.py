class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Ho")


d1 = Dog("Brownie", 2)
d1.speak()
print(d1.name)
print(d1.age)

