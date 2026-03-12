import numpy as np
from core.qubit import zero_state, normalize
from core.gates import I

class Simulator:

    def __init__(self, circuit):

        self.circuit = circuit
        self.n = circuit.n
        self.state = zero_state(self.n)

    def expand_gate(self, gate, target):

        full = 1

        for i in range(self.n):

            if i == target:
                op = gate
            else:
                op = I

            if isinstance(full, int):
                full = op
            else:
                full = np.kron(full, op)

        return full


    def apply_cnot(self, control, target):

        size = 2**self.n
        new_state = np.zeros(size, dtype=complex)

        for i in range(size):

            if (i >> control) & 1:
                flipped = i ^ (1 << target)
                new_state[flipped] += self.state[i]
            else:
                new_state[i] += self.state[i]

        self.state = new_state


    def run(self):

        for op in self.circuit.operations:

            if op["type"] == "single":

                gate = op["gate"]
                target = op["target"]

                full = self.expand_gate(gate, target)
                self.state = full @ self.state

            elif op["type"] == "cnot":

                self.apply_cnot(op["control"], op["target"])

        self.state = normalize(self.state)

        return self.state


    # 🔹 NEW FUNCTION
    def measure(self, shots=1000):

        probs = np.abs(self.state)**2

        states = np.arange(len(probs))

        samples = np.random.choice(states, size=shots, p=probs)

        results = {}

        for s in samples:

            bitstring = format(s, f"0{self.n}b")

            if bitstring not in results:
                results[bitstring] = 0

            results[bitstring] += 1

        return results
