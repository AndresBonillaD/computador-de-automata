# way to navigate the app
from Entity.DFA import DFA
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

# alphabet dict
a = {'a', 'b'}
# states dict
s = {q0, q1}
# initial state q0
# instance dfa object
fda0 = DFA(a, s, q0)

print('-- done --')
fda0.showData()
