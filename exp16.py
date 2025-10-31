# Quantum Algorithm and Computational Methods
# Program: Grover’s Algorithm to search for |11⟩ in a 2-qubit system

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from IPython.display import display

def grover_search_2qubit(marked_state='11', shots=1024):
    qc = QuantumCircuit(2, 2)

    # Step 1: Initialize both qubits in superposition using Hadamard gates
    qc.h([0, 1])

    # Step 2: Oracle for |11⟩ → flips the phase of the marked state
    qc.cz(0, 1)

    # Step 3: Diffusion operator (inversion about the mean)
    qc.h([0, 1])
    qc.x([0, 1])
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    qc.x([0, 1])
    qc.h([0, 1])

    # Step 4: Measure both qubits
    qc.measure([0, 1], [0, 1])

    # Simulate
    sim = AerSimulator()
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()

    # Display results
    print(f"\nGrover’s Algorithm to find |{marked_state}⟩")
    display(qc.draw('mpl'))
    print(f"Expected Output: Highest probability for |{marked_state}⟩")
    print("Measurement Counts:", counts)

# Run the program
grover_search_2qubit()

