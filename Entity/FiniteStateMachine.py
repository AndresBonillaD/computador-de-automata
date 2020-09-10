# class for deterministic finite automata
# initial state attribute is a string to be compared with the tag attribute of states
from Entity.State import State


class FiniteStateMachine:
    alphabet = set()
    states = set()
    initialState = State
    controlUnit = State

    def __init__(self, alphabet, states, initialState):
        self.alphabet = alphabet
        self.states = states
        self.initialState = initialState
        self.controlUnit = self.initialState

    # block to process strings
    def computeWord(self, word):
        print('Computing string: "{0}" , Length: {1} ...'.format(word, len(word)))

        if len(word) == 1:
            # base case
            print('base case')
            # change control unit
            for tr in self.controlUnit.transitions:
                if tr.symbol == word[0]:
                    print('- Transition found: {0}:{1}>{2}'.format(tr.currentState, tr.symbol, tr.destinyState))
                    print('change control unit to {0}'.format(tr.destinyState))
                    # change control unit
                    self.controlUnit = self.controlUnitChange(tr.destinyState)

            if self.controlUnit.isAccepted:
                print('ACCEPTED STRING! the state {0} is Accepted.'.format(self.controlUnit.tag))
            else:
                print('REJECTED STRING state {0} is NOT Accepted'.format(self.controlUnit.tag))
        else:
            # recursive case
            # change control unit
            print('recursive case')
            print('Control Unit: {0} symbol to process: {1}'.format(self.controlUnit.tag, word[0]))
            for tr in self.controlUnit.transitions:
                if tr.symbol == word[0]:
                    print('- Transition found: {0}:{1}>{2}'.format(tr.currentState, tr.symbol, tr.destinyState))
                    print('- change control unit to {0}'.format(tr.destinyState))
                    self.controlUnit = self.controlUnitChange(tr.destinyState)
                    self.computeWord(word[1:])



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

    # return a state from a tag
    def controlUnitChange(self, tag):
        for state in self.states:
            if tag == state.tag:
                return state
