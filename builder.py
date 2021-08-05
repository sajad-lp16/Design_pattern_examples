from abc import ABCMeta, abstractmethod


# BUILDERS ----------------------------------------------
class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    hp = None


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_body(self):
        pass


class Benz(Builder):
    def get_body(self):
        body = Body()
        body.shape = 'Benz Shape'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 330
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel


# PRODUCT ----------------------------------------------
class Car:
    __wheel = None
    __body = None
    __engine = None

    @property
    def wheel(self):
        return self.__wheel

    @wheel.setter
    def wheel(self, wheel):
        self.__wheel = wheel

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    def show_details(self):
        return f'Body = {self.__body.shape}\n' \
               f'Engine = {self.__engine.hp}\n' \
               f'Wheel = {self.__wheel.size}\n'


# DIRECTOR -------------------------------------------
class Director:
    __builder = None

    def __init__(self, builder):
        self.__builder = builder

    def create_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.body = body

        engine = self.__builder.get_engine()
        car.engine = engine

        wheel = self.__builder.get_wheel()
        car.wheel = wheel

        return car


b = Benz()
d = Director(b)
mine = d.create_car()
print(mine.show_details())
