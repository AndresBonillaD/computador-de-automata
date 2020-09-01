# class for deterministic finite automata
# initial state attribute is a string to be compared with the tag attribute of states
from Entity.State import State


class DFA:
    alphabet = {}
    states = {}
    initialState = State

    def __init__(self, alphabet, states, iniState):
        self.alphabet = alphabet
        self.states = states
        self.initialState = iniState

    # method to print on console the info representing the automata
    def showData(self):
        print('#alphabet')
        for symbol in self.alphabet:
            print(symbol)
        print('#states')
        for state in self.states:
            print(state.tag)
        print('#initial')
        print(self.initialState.tag)
        print('#accepting')
        for state in self.states:
            if state.isAccepted: print(state.tag)
        print('#transitions')
        print('cs ds s')
        for state in self.states:
            for tr in state.transitions:
                print(tr.currentState, tr.destinyState, tr.symbol)
