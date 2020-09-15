# class fr estate element
class State:
    # transitions data structure to define
    # transitions can be made by using dictionaries {'symbol' : [DestinyStates]}
    tag = ''
    isAccepted = False
    transitions = list()

    def __init__(self, tag, accepted, transitions):
        self.tag = tag
        self.isAccepted = accepted
        self.transitions = transitions
