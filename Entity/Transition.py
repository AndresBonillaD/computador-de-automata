# class for transitions
class Transition:
    currentState = ''
    destinyState = ''
    symbol = ''

    def __init__(self, cs, ds, s):
        self.currentState = cs
        self.destinyState = ds
        self.symbol = s
