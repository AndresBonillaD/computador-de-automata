# class fr estate element
class State:
    tag = ''
    isAccepted = False
    transitions = []

    def __init__(self, tag, accepted, transitions):
        self.tag = tag
        self.isAccepted = accepted
        self.transitions = transitions
