class Iteration:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        if self.value == 0:
            raise StopIteration('End of sequence ...')
        for i in range(self.value):
            value = self.value
            self.value -= 1
            return value


class Iterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        value = Iteration(self.value)
        return value


if __name__ == '__main__':
    f = Iterable(10)
    d = f.__iter__()
    print(d.__next__())
    print(d.__next__())
    print(d.__next__())
