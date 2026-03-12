import numpy as np

# Identity
I = np.eye(2, dtype=complex)

# Pauli gates
X = np.array([[0,1],[1,0]], dtype=complex)

Y = np.array([[0,-1j],[1j,0]], dtype=complex)

Z = np.array([[1,0],[0,-1]], dtype=complex)

# Hadamard
H = (1/np.sqrt(2)) * np.array([
    [1,1],
    [1,-1]
], dtype=complex)

# Phase
S = np.array([
    [1,0],
    [0,1j]
], dtype=complex)

# T gate
T = np.array([
    [1,0],
    [0,np.exp(1j*np.pi/4)]
], dtype=complex)

# CNOT
CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
], dtype=complex)
