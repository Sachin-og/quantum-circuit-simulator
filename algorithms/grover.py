import numpy as np
import math

from core.circuit import QuantumCircuit
from core.simulator import Simulator
from core.gates import H


def run():

    print("\nGeneral Grover Search\n")

    n = int(input("Enter number of qubits: "))
    target = input("Enter target bitstring: ")

    if len(target) != n:
        print("Target length must match qubit count")
        return

    N = 2**n
    target_index = int(target,2)

    # Create circuit
    qc = QuantumCircuit(n)

    for i in range(n):
        qc.add_gate(H,i)

    sim = Simulator(qc)

    state = sim.run()

    # Optimal number of Grover iterations
    iterations = int((math.pi/4) * math.sqrt(N))

    print("\nGrover iterations:", iterations)

    for _ in range(iterations):

        # Oracle
        state[target_index] *= -1

        # Diffusion
        avg = np.mean(state)

        for i in range(len(state)):
            state[i] = 2*avg - state[i]

    # Normalize
    state = state / np.linalg.norm(state)

    sim.state = state

    print("\nState Vector (significant amplitudes):\n")

    for i,amp in enumerate(state):

        if abs(amp) > 0.05:

            print(f"|{format(i,f'0{n}b')}> : {amp}")

    print("\nMeasurement Results (1000 shots):\n")

    results = sim.measure(1000)

    for k,v in sorted(results.items()):

        print(k,":",v)
