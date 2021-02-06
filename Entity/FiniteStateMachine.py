# class for deterministic finite automata
# initial state attribute is a string to be compared with the tag attribute of states
from Entity.State import State


# control unit stores the current state the machine has during a process
class FiniteStateMachine:
    alphabet = set()
    states = set()
    initialState = State
    controlUnit = State

    accepted = 0

    # constructor of the class fsm
    def __init__(self, alphabet, states, initialState):
        self.alphabet = alphabet
        self.states = states
        self.initialState = initialState
        self.controlUnit = self.initialState

    # block to process strings
    # frontier case, empty word!!!!!!!!
    def computeWord(self, word):
        remaningSymbol = False

        print('Computing string: "{0}" , Length: {1} ...'.format(word, len(word)))
        print('- - -')
        if len(word) == 0:
            print("cadena vacia")
        elif len(word) == 1:
            #### BASE CASE
            print('base case')
            print('Control Unit: {0}.   Symbol to process: {1}'.format(self.controlUnit.tag, word[0]))

            # change control unit - last one to process the end symbol in the word
            if str(word[0]) not in self.controlUnit.transitions:
                print('NO transition found')
                remaningSymbol = True
            else:
                # change the CU to the only destinyState (dfa)
                desStates = self.controlUnit.transitions[word[0]]
                print('Transition Found: {0}:{1}>{2}'.format(self.controlUnit.tag, word[0], desStates[0]))
                print('- - -')
                # simulate CONSUME SYMBOL
                self.controlUnit = self.controlUnitChange(desStates[0])

            # check for the final state reached in the machine and for remaining symbols in the string
            # satisfaction conditions for Acceptance of the word
            if self.controlUnit.isAccepted and not remaningSymbol:
                print('ACCEPTED STRING! the state {0} is Accepted.'.format(self.controlUnit.tag))
            else:
                print('REJECTED STRING state {0} is NOT Accepted'.format(self.controlUnit.tag))
        else:
            #### RECURSIVE CASE
            # change CU to the destiny states in the transitions dict in the current CU
            print('recursive case')
            print('Control Unit: {0}.   Symbol to process: {1}'.format(self.controlUnit.tag, word[0]))

            # check the possibility of computing the first symbol of word
            if word[0] not in self.controlUnit.transitions:
                    print('NO transitions found for {0}:{1}'.format(self.controlUnit.tag, word[0]))
                    print('REJECTED STRING')
                    #retur 0
            else:
                # change the CU to the only destinyState (dfa)
                # desStates = [ possible states to go with transition word[0] ]
                desStates = self.controlUnit.transitions[word[0]]
                print('Transition Found: {0}:{1}>{2}'.format(self.controlUnit.tag, word[0], desStates[0]))
                print('- - -')
                self.controlUnit = self.controlUnitChange(desStates[0])
                # recursive calling CONSUME SYMBOL
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

    # return a state from a tag string
    def controlUnitChange(self, tag):
        for state in self.states:
            if tag == state.tag:
                return state