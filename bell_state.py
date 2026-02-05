from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Step 1: Create a Quantum Circuit
qc = QuantumCircuit(2, 2)
qc.h(0)              # Put qubit 0 in superposition
qc.cx(0, 1)          # Entangle qubit 0 with qubit 1
qc.measure([0,1], [0,1])  # Measure both qubits

print("Quantum Circuit:")
print(qc)

# Step 2: Use Local Simulator
simulator = AerSimulator()

# Transpile circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Step 3: Run the simulation
result = simulator.run(compiled_circuit, shots=1024).result()

# Step 4: Get results
counts = result.get_counts(qc)
print("\nSimulation Results:", counts)
