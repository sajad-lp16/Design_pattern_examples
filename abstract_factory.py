from abc import ABCMeta, abstractmethod


# ABSTRACT FACTORY ------------------------------------
class Car(metaclass=ABCMeta):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


# -----------------------------------------------------
class BMW(Car):
    def call_suv(self):
        return X1()

    def call_coupe(self):
        return M2()


class Benz(Car):
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()


# PRODUCT FACTORIES--------------------------------------
class SuvFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_suv(self):
        pass


class CoupeFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_coupe(self):
        pass


class X1(SuvFactory):
    def create_suv(self):
        return 'This is Your Suv from BMW'


class Gla(SuvFactory):
    def create_suv(self):
        return 'This is Your Suv from Benz'


class M2(CoupeFactory):
    def create_coupe(self):
        return 'This is Your coupe from BMW'


class Cls(CoupeFactory):
    def create_coupe(self):
        return 'This is Your coupe from Benz'


# CLIENT ------------------------------------------------

CAR_MODELS = {
    'benz': Benz,
    'bmw': BMW
}


class Client:
    def __init__(self, name):
        self.name = name

    def client_suv(self, car):
        return car.call_suv().create_suv()

    def client_coupe(self, car):
        return car.call_coupe().create_coupe()

    def get_order(self, company, model):
        car = CAR_MODELS[company]()
        if model == 'suv':
            return self.client_suv(car)
        elif model == 'coupe':
            return self.client_coupe(car)


print()
