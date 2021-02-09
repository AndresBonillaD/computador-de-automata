from Entity.FiniteStateMachine import FiniteStateMachine

class AutomataController:


    def automataMenuLoop(self, automata):
        case = ''

        while case != 'exit':
            case = self.switcher()
            print('Case:', case)

            if case == 'CW':
                word = input('Type the word to be used: ')
                res = automata.computeWord(word)
                automata.wordList[word] = res
                print(' resultado: ')
                print(automata.wordList)
                # restores the control unit to the initial position
                automata.controlUnit = automata.initialState
                continue
            if case == 'showdata':
                automata.showData()
                continue
            if case == 'exit':
                print('### exit Automata ###')
                continue
            if case == 'nothing':
                print('INVALID COMMAND')
                continue

    def switcher(self):

        switcher = {
            '1': 'CW',
            '2': 'showdata',
            '3': '',
            '4': '',
            'exit': 'exit'
        }

        print('-----   Automata Menu   -----')
        print('''
        1: Compute Word
        2: Show Automata Data
        3: ...
        4: ...
        exit: salir
            ''')

        argument = input('Ingrese comando: ')
        return switcher.get(argument, 'nothing')
