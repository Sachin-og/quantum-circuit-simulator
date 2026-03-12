import numpy as np

def zero_state(n):
    """
    Create |00...0> state for n qubits
    """
    state = np.zeros(2**n, dtype=complex)
    state[0] = 1
    return state

def normalize(state):
    norm = np.linalg.norm(state)
    if norm == 0:
        return state
    return state / norm

def measure(state):
    """
    Returns measurement outcome
    """
    probs = np.abs(state)**2
    outcome = np.random.choice(len(state), p=probs)
    return outcome, probs
