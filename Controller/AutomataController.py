from Entity.FiniteStateMachine import FiniteStateMachine


class AutomataController:

    #  {string:bool}
    wordList = dict()



    def automataMenuLoop(self, automata):
        case = ''

        while case != 'exit':
            case = self.switcher()
            print('Case:', case)

            if case == 'CW':
                word = input('Type the word to be used: ')
                automata.computeWord(word)
                continue
            if case == 'exit':
                print('### exit Automata ###')
                continue
            if case == 'nothing':
                print('INVALID COMMAND')
                continue

    def switcher(self):

        switcher = {
            '0': 'CW',
            '1': 'case1',
            '2': '',
            '3': '',
            'exit': 'exit'
        }

        print('-----   Automata Menu   -----')
        print('''
        0: ComputeWord
        1: ...
        2: ...
        3: ...
        exit: salir
            ''')

        argument = input('Ingrese comando: ')
        return switcher.get(argument, 'nothing')
