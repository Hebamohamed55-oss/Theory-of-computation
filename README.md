# 🧠 Automata Theory Final Projects – Heba mohamed hassan 
# sec 6 
# IDNumber : 4580

This repository contains two complete projects implemented in Python as part of the Automata Theory course.

## 🔧 Contents

- **Project 1: DFA Equivalence Checker**
- **Project 2: CYK Parser for CFG in CNF**

---

## 📁 Project 1: DFA Equivalence Checker

### 📌 Objective
Check whether two Deterministic Finite Automata (DFAs) accept the same language.

### 🧠 How it Works
- Each DFA is represented by its set of states, alphabet, transition function, start state, and accept states.
- The `accepts` function simulates the DFA on an input string.
- The `are_equivalent` function checks all possible strings up to a maximum length (default: 5) to verify if both DFAs accept the same strings.

### 🧪 Example

```python
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
