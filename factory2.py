from abc import ABCMeta, abstractmethod


# CREATE -------------------------------
class Creator(metaclass=ABCMeta):

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        _instance = self.make()
        return _instance.edit()


class XMLCreator(Creator):

    def make(self):
        return XML()


class JSONCreator(Creator):

    def make(self):
        return JSON()


# PRODUCT ----------------------------------------
class Product(metaclass=ABCMeta):

    @abstractmethod
    def edit(self):
        pass


class XML(Product):
    def edit(self):
        return 'Editing XML file ...'


class JSON(Product):
    def edit(self):
        return 'Editing JSON file ...'


# CLIENT ----------------------------------------

class Client:
    def __init__(self, format):
        self.obj = JSONCreator() if format == 'json' else XMLCreator()

    def start_process(self):
        return self.obj.call_edit()
