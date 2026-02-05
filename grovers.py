from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Step 1: Create Grover's Circuit (searching for |11>)
qc = QuantumCircuit(2, 2)

# Initialize into superposition
qc.h([0, 1])

# Oracle for |11> (phase flip)
qc.cz(0, 1)

# Diffuser (inversion about the mean)
qc.h([0, 1])
qc.x([0, 1])
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x([0, 1])
qc.h([0, 1])

# Measure
qc.measure([0, 1], [0, 1])
print("Grover's Algorithm Quantum Circuit:")
print(qc)

# Step 2: Use Local Simulator
simulator = AerSimulator()

# Transpile circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Step 3: Run the simulation
result = simulator.run(compiled_circuit, shots=1024).result()

# Step 4: Get results
counts = result.get_counts(qc)
print("\nGrover's Algorithm Results:", counts)
