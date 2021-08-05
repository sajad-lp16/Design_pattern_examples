class IranSocket:
    _pin_type = '2'


class Adapter:
    _socket = None
    _pin_type = '3To2'

    def __init__(self, socket):
        self._socket = socket


class Fridge:
    _pin_type = '3'
    _adapter = None

    def __init__(self, adapter):
        self._adapter = adapter

    def freeze(self):
        if self._adapter._pin_type == self._pin_type + 'To' + self._adapter._socket._pin_type:
            print('Done ...')
        else:
            print('It doesnt work')


s = IranSocket()
a = Adapter(s)
f = Fridge(a)
f.freeze()
