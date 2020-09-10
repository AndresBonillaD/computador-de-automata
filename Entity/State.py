# class fr estate element
class State:
    # transitions data structure to define
    tag = ''
    isAccepted = False
    transitions = list()

    def __init__(self, tag, accepted, transitions):
        self.tag = tag
        self.isAccepted = accepted
        self.transitions = transitions
