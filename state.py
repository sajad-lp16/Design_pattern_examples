class State:
    def operate(self):
        print(f'Turning Tv {self.status}')


class TurnOn(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'On'

    def change_state(self):
        print('Changing state to off')
        self.tv.state = self.tv.off


class TurnOff(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'Off'

    def change_state(self):
        print('Changing state to Off')
        self.tv.state = self.tv.off


class Tv:
    def __init__(self):
        self.on = TurnOn(self)
        self.off = TurnOff(self)
        self.state = self.on

    def press(self):
        self.state.operate()
        self.state.change_state()


tv = Tv()
tv.press()
