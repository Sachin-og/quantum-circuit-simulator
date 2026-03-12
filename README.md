# quantum-circuit-simulator

A lightweight **quantum circuit simulator written from scratch in Python** that demonstrates fundamental quantum computing concepts such as **superposition, entanglement, measurement, and quantum algorithms**.

This project was built to understand the internal mechanics of quantum simulators instead of relying on high-level frameworks.

---

## Overview

Quantum computers operate on **qubits** instead of classical bits.

A qubit can exist in a **superposition of states**:

|ψ⟩ = α|0⟩ + β|1⟩

where:

- α and β are complex amplitudes
- |α|² + |β|² = 1

This simulator models quantum states as **complex vectors** and applies quantum gates through **matrix transformations**.

---

## Features

- Quantum state vector simulation
- Implementation of common quantum gates
- Multi-qubit circuit construction
- Measurement simulation using probabilistic sampling
- Implementations of important quantum states and algorithms

Implemented circuits:

- Bell State Generator
- GHZ State Generator
- Grover Search Algorithm

---

## Project Structure

quantum-circuit-simulator
│
├── core
│ ├── circuit.py # Quantum circuit construction
│ ├── gates.py # Gate matrix definitions
│ └── simulator.py # State evolution and measurement
│
├── algorithms
│ ├── bell.py # Bell state generation
│ ├── ghz.py # GHZ state generator
│ └── grover.py # Grover search algorithm
│
├── main.py # Interactive CLI interface
└── README.md


---

## Bell State

Bell states are the simplest example of **quantum entanglement**.

Circuit:

q0 ──H──●──
│
q1 ─────X──


Resulting state:

(|00⟩ + |11⟩) / √2

This means the two qubits are **perfectly correlated**.

---

## GHZ State

A GHZ state generalizes entanglement to **multiple qubits**.

Circuit:

q0 ──H──●────────
│
q1 ─────X──●─────
│
q2 ────────X──●──
│
q3 ───────────X──


Resulting state:
(|000...0⟩ + |111...1⟩) / √2

GHZ states are used in **quantum communication and quantum error correction**.

---

## Grover Search Algorithm

Grover's algorithm provides **quadratic speedup** for searching an unstructured database.

Classical complexity: O(N)

Quantum complexity: O(√N)

The simulator allows the user to choose which basis state to **amplify** during the Grover iteration.

Example output:

Grover Search (2 Qubits)

Target state: 10

Measurement Results (1000 shots)

10 : 820
00 : 60
01 : 55
11 : 65


The correct state appears with **highest probability**.

---

## Running the Simulator

Clone the repository:

git clone https://github.com/Sachin-og/quantum-circuit-simulator.git


Navigate to the project directory:

cd quantum-circuit-simulator

Run the Simulator: python main.py

Interactive menu:

1. Bell State
2. GHZ State
3. Grover Search

---

## Example Output

Quantum Circuit Simulator

Bell State

GHZ State

Grover Search

Enter choice: 1

Bell State

|00> : 0.7071
|11> : 0.7071

Measurement Results (1000 shots)

00 : 502
11 : 498


---

## Concepts Demonstrated

This project demonstrates the core building blocks of quantum computing:

- Superposition
- Entanglement
- Quantum measurement
- Quantum interference
- Quantum algorithm design

---

## Future Improvements

Planned extensions:

- Additional gates (T, S, Controlled gates)
- Quantum teleportation protocol
- Deutsch–Jozsa algorithm
- Noise simulation and decoherence
- Circuit visualization
- Integration with larger qubit systems

---

## Motivation

The goal of this project is to **build intuition about quantum computing systems by implementing them from first principles** rather than using high-level libraries.

Understanding how simulators work internally provides deeper insight into:

- Quantum algorithm behavior
- State evolution
- Measurement probabilities
- Quantum circuit architecture

---

## Author

Sachin Aggarwal  

GitHub  
https://github.com/Sachin-og