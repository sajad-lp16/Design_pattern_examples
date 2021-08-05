from copy import deepcopy


class Product:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        copy_obj = deepcopy(self._objects[name])
        copy_obj.__dict__.update(*kwargs)
        return copy_obj


a = Product('django', 'python', 20)
b = Prototype()
b.register('a',a)
c = b.clone('a')
print(c.name)