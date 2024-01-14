class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} hii')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


d1 = Dog("Jay")
d1.make_sound()
