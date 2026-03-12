from core.circuit import QuantumCircuit
from core.simulator import Simulator
from core.gates import H


def run():

    qc = QuantumCircuit(2)

    qc.add_gate(H, 0)
    qc.add_cnot(0, 1)

    sim = Simulator(qc)

    state = sim.run()

    print("\nState Vector:\n")

    for i, amp in enumerate(state):

        if abs(amp) > 1e-6:
            print(f"|{format(i,'02b')}> : {amp}")

    print("\nMeasurement Results (1000 shots):\n")

    results = sim.measure(1000)

    for k,v in results.items():
        print(k,":",v)
