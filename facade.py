class Raw:
    @staticmethod
    def raw():
        print('Buying stuff from the market')


class Transfer:
    @staticmethod
    def transfer():
        print('transferring stuff to the restaurant')


class Cook:
    @staticmethod
    def cook():
        print('cooking food')


class Serve:
    @staticmethod
    def serve():
        print('serving food to the client')


class ItalianRestaurant:
    @staticmethod
    def get():
        raw = Raw()
        raw.raw()

        transfer = Transfer()
        transfer.transfer()

        cook = Cook()
        cook.cook()

        serve = Serve()
        serve.serve()


def order():
    restaurant = ItalianRestaurant()
    restaurant.get()


if __name__ == '__main__':
    order()
