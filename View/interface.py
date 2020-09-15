# way to navigate the app
from Controller.AutomataFileReader import AutomataFileReader
from Entity.FiniteStateMachine import FiniteStateMachine
from Entity.State import State
from Entity.Transition import Transition

# hardcoded dfa
# instance transitions
t0 = Transition('q0', 'q0', 'a')
t1 = Transition('q0', 'q1', 'b')
t2 = Transition('q1', 'q1', 'b')
# instance states
q0 = State('q0', False, [t0, t1])
q1 = State('q1', True, [t2])

# alphabet set
a = {'a', 'b'}
# states set
s = {q0, q1}
# initial state q0
# instance dfa object
fda0 = FiniteStateMachine(a, s, q0)

# start

#fda0.showData()
print()
fda0.computeWord('ab')
#fileReader = AutomataFileReader()
#fileReader.openFile()
