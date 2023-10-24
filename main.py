# backend
from qiskit import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with the actual origin of your front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#compute function:
def compute(grover_circ):
    backend = Aer.get_backend('qasm_simulator')
    result_string = '00000000'
    trials = 0
    while result_string != '11111111':
        job = execute(grover_circ, backend, shots=1)
        result = job.result()
        result_counts = result.get_counts()
        trials = trials + 1
        # print(f"current count:{trials}, result : {result_counts}")
        result_string = list(result_counts.keys())[0]
# Print the result
    print(result_string)
    print(f"total trials {trials}")
    return trials

# developing circuit:
# Define the Oracle Circuit
oracle = QuantumCircuit(8, name='oracle')
oracle.cz(0, 7)  # Apply a controlled-Z gate between qubits 0 and 7
oracle.to_gate()

# Define the Reflection Circuit
reflection = QuantumCircuit(8, name='reflection')
reflection.h(range(8))
reflection.z(range(8))
reflection.cz(0, 7)  # Apply a controlled-Z gate between qubits 0 and 7
reflection.h(range(8))
reflection.to_gate()

# Set Up the Grover's Algorithm Circuit
grover_circ = QuantumCircuit(8, 8)
grover_circ.h(range(8))
grover_circ.append(oracle, range(8))
grover_circ.append(reflection, range(8))
grover_circ.measure(range(8), range(8))
# Write the circuit code here
# b = 77 
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Quantum App!"}

@app.get("/result/")
async def comparisons():
    result = compute(grover_circ)
    # Write the iteration code here
    return {"result": result}

# uvicorn main:app --reload