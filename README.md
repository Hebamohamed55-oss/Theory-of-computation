# 🧠 Automata Theory Final Projects – Heba Mohamed hassan 
# sec 6
# IDNumber : 4580

This repository contains two complete Python projects implemented for the **Automata Theory** course:

- ✅ **Project 1:** DFA Equivalence Checker  
- ✅ **Project 2:** CYK Parser for CFG in CNF  

Both projects are written in pure Python and require no external libraries.

---

## 📁 Project 1: DFA Equivalence Checker

### 📌 Objective
Check whether two DFAs (Deterministic Finite Automata) accept the **same language** by testing all strings up to a given length.

### 🧠 How It Works
- A class `DFA` is used to define the automaton's structure.
- The `accepts` method simulates the DFA on a given string.
- The function `are_equivalent(dfa1, dfa2)` generates all strings (up to length 5 by default) using the alphabet and compares acceptance results of both DFAs.


# Sample DFAs
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

print(are_equivalent(dfa1, dfa2))  # Output: True


📁 Project 2: CYK Parser for CFG in CNF
📌 Objective
Use the CYK Algorithm to determine whether a given string is part of a language defined by a Context-Free Grammar (CFG) in Chomsky Normal Form (CNF).

🧠 How It Works
Grammar is represented as a dictionary: each non-terminal maps to a list of productions (tuples).

The CYK table is built bottom-up.

If 'S' (start symbol) exists in the top-right cell, then the string is accepted.



# Example Grammar in CNF
grammar = {
    'S': [('A', 'B'), ('B', 'A')],
    'A': [('a',)],
    'B': [('b',)]
}

string = "ab"
print(CYK_parser(grammar, string))  # Output: True
