def draw(circuit):

    lines = [["---"]*len(circuit.operations) for _ in range(circuit.n)]

    for step, op in enumerate(circuit.operations):

        if op["type"] == "single":

            lines[op["target"]][step] = "[G]"

        elif op["type"] == "cnot":

            lines[op["control"]][step] = "[C]"
            lines[op["target"]][step] = "[X]"

    for i in range(circuit.n):

        print("q",i," :", " ".join(lines[i]))
