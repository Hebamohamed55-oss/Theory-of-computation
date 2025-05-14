class DFA:
    def init(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol not in self.alphabet:
                return False 
            current_state = self.transition_function[current_state][symbol]
        return current_state in self.accept_states

def are_equivalent(dfa1, dfa2):
  
    max_length = 5 
    from itertools import product
    
    alphabet = dfa1.alphabet
    for length in range(1, max_length + 1):
        for string_tuple in product(alphabet, repeat=length):
            string = ''.join(string_tuple)
            if dfa1.accepts(string) != dfa2.accepts(string):
                return False
    return True


dfa1 = DFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b'},
    transition_function={
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q0', 'b': 'q2'},
        'q2': {'a': 'q2', 'b': 'q1'}
    },
    start_state='q0',
    accept_states={'q1'}
)

dfa2 = DFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b'},
    transition_function={
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q0', 'b': 'q2'},
        'q2': {'a': 'q2', 'b': 'q1'}
    },
    start_state='q0',
    accept_states={'q1'}
)

print(are_equivalent(dfa1, dfa2))
