# class for transitions
class Transition:
    # destinyState can be one or multiple states
    currentState = ''
    destinyState = list()
    symbol = ''

    def __init__(self, cs, ds, s):
        self.currentState = cs
        self.destinyState = ds
        self.symbol = s
