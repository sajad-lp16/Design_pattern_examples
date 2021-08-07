from abc import ABCMeta, abstractmethod


class World(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name
        self.children = []

    @abstractmethod
    def show(self):
        pass

    def add(self, obj):
        self.children.append(obj)

    def remove(self, obj):
        self.children.remove(obj)


class Being(World):

    def show(self):
        print(f'Being Composite {self.name}')
        for child in self.children:
            child.show()


class AnimalComposite(Being):

    def show(self):
        print(f'\tAnimal Composite {self.name}')
        for child in self.children:
            child.show()


class HumanComposite(Being):

    def show(self):
        print(f'\tHuman Composite {self.name}')
        for child in self.children:
            child.show()


class Leaf(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show(self):
        pass


class Human(Leaf):

    def show(self):
        print(f'\t\tThe name of human is {self.name}')


class Animal(Leaf):
    def show(self):
        print(f'\t\tThe name of animal is {self.name}')


class Male(Human):
    pass


class Female(Human):
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


if __name__ == '__main__':
    a1 = Cat('Catty')
    a2 = Dog('Doggy')

    h1 = Male('Mehdi')
    h2 = Female('Nazanin')

    ac = AnimalComposite('Animal Composite1')
    hc = HumanComposite('Human Composite1')

    ac.add(a1)
    ac.add(a2)

    hc.add(h1)
    hc.add(h2)

    bc = Being('Being Composite')
    bc.add(hc)
    bc.add(ac)

    bc.show()

    print(ac.children)
    print(hc.children)
