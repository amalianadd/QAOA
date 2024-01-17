# Langkah 1: Instalasi Qiskit
# Pastikan Anda telah menginstal Qiskit di lingkungan Python Anda. Anda dapat menginstalnya menggunakan perintah pip:
# pip install qiskit

from qiskit import QuantumCircuit, transpile, Aer, assemble
from qiskit.visualization import plot_histogram
from qiskit.aqua.operators import WeightedPauliOperator
from qiskit.aqua.components.optimizers import COBYLA
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA

# Langkah 2: Mendefinisikan Masalah (Contoh: Max-Cut)
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # Daftar edge dalam graf
weights = [1.0, 1.0, 1.0, 1.0]  # Daftar bobot untuk setiap edge

# Langkah 3: Membuat Operator Hamiltonian
pauli_dict = {
    'paulis': [{"coeff": {"real": w, "imag": 0.0}, "label": f"Z{i}Z{j}"}
               for (w, (i, j)) in zip(weights, edges)]
}

problem_operator = WeightedPauliOperator.from_dict(pauli_dict)

# Langkah 4: Membuat Sirkuit QAOA
num_qubits = len(problem_operator.print_details()['paulis'])
p = 1  # Jumlah lapisan QAOA

qaoa_circuit = QuantumCircuit(num_qubits)
qaoa_circuit += problem_operator.evolve(
    evo_time=0, num_time_slices=p, quantum_registers=qaoa_circuit.qregs[0])

# Langkah 5: Menyiapkan Algoritma QAOA
optimizer = COBYLA(maxiter=100)
qaoa = QAOA(problem_operator, optimizer, p)

# Langkah 6: Menjalankan Algoritma QAOA
backend = Aer.get_backend('statevector_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)

result = qaoa.run(quantum_instance)

# Langkah 7: Menampilkan Hasil
optimal_params = result['optimal_parameters']
optimal_cost = result['optimal_value']

print(f"Optimal Parameters: {optimal_params}")
print(f"Optimal Cost: {optimal_cost}")

plot_histogram(result['eigenstate']).show()
