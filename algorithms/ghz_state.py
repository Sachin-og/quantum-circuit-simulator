import numpy as np

from core.circuit import QuantumCircuit
from core.simulator import Simulator
from core.gates import H


def run():

    print("\n========== GHZ State Generator ==========\n")

    n = int(input("Enter number of qubits (>=2): "))

    if n < 2:
        print("GHZ requires at least 2 qubits")
        return

    print(f"\nBuilding GHZ circuit for {n} qubits...\n")

    qc = QuantumCircuit(n)

    # Step 1: create superposition on first qubit
    qc.add_gate(H,0)

    # Step 2: chain of CNOTs to entangle qubits
    for i in range(n-1):
        qc.add_cnot(i, i+1)

    sim = Simulator(qc)

    state = sim.run()

    print("\nState Vector (non-zero amplitudes):\n")

    for i,amp in enumerate(state):

        if abs(amp) > 1e-6:

            print(f"|{format(i,f'0{n}b')}> : {amp}")

    print("\nMeasurement Results (1000 shots):\n")

    results = sim.measure(1000)

    for k,v in sorted(results.items()):
        print(k,":",v)

    print("\nExpected GHZ basis states:")
    print("0"*n, "and", "1"*n)

    print("\n========================================\n")
