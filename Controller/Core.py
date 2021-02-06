from Entity.FiniteStateMachine import FiniteStateMachine
from Entity.State import State


class core:
    #att

    #### MENU

    def menuLoop(self):
        case = ''

        while case != 'exit':
            case = self.switcher()
            print('Case:', case)

            if case == 'case0':
                print('futura carga de archivo .txt')
                continue
            if case == 'case1':
                print('futura carga de automata manualmente')
                continue
            if case == 'automataDemo':
                print('hardcoded fsm')

                # hardcoded dfa L = { a*b+ }
                # instance transitions
                q0Transitions = {'a': ['q0'], 'b': ['q1']}
                q1Transitions = {'b': ['q1']}
                # instance states
                q0 = State('q0', False, q0Transitions)
                q1 = State('q1', True, q1Transitions)
                # alphabet set
                a = {'a', 'b'}
                # states set
                s = {q0, q1}
                # initial state q0
                # instance dfa object
                fda0 = FiniteStateMachine(a, s, q0)

                # fda0.showData()
                word = input('Compute word: ')
                word_process = fda0.computeWord(word)
                print(word_process)


                continue
            if case == 'nothing':
                print('NO SUCH COMMAND')
                continue

    # return the specific command corresponding to the user input
    def switcher(self):

        switcher = {
            '0': 'case0',
            '1': 'case1',
            '2': 'automataDemo',
            'exit': 'exit'
        }

        print('-----   Menu   -----')
        print('''
        0: Case0
        1: case1
        2: Automata Demo
        exit: salir
            ''')

        argument = input('Ingrese comando: ')

        return switcher.get(argument, 'nothing')