class Observer:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class One:
    def update(self, obj):
        print(f'The value of {obj.name} was changed to {obj.data}')


class Two:
    def update(self, obj):
        print(f'The value of {obj.name} was changed to {obj.data}')


a = Data('first')
b = Data('second')

x = One()
y = Two()

a.attach(x)
b.attach(y)

a.data = 20
b.data = 30
