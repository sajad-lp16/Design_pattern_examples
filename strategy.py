from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, direction, text):
        self._direction = direction
        self._text = text

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    def sort(self):
        return self._direction.direct(self._text)


class Direction(ABCMeta):
    @abstractmethod
    def direct(self):
        pass


class Right:
    @staticmethod
    def direct(data):
        print(data[::-1])


class Left:
    @staticmethod
    def direct(data):
        print(data)


def strategy():
    right = Left()
    context = Context(right, 'Hello')
    context.sort()


if __name__ == '__main__':
    strategy()
