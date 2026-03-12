class QuantumCircuit:

    def __init__(self, n_qubits):

        self.n = n_qubits
        self.operations = []

    def add_gate(self, gate, target):

        self.operations.append({
            "type": "single",
            "gate": gate,
            "target": target
        })

    def add_cnot(self, control, target):

        self.operations.append({
            "type": "cnot",
            "control": control,
            "target": target
        })
