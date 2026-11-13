import stim

circuit = stim.Circuit()
circuit.append("X_ERROR", [0], 0.001)
circuit.append("Y_ERROR", [0], 0.001)
circuit.append("Z_ERROR", [0], 0.008)

print(circuit)
