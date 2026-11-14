# XZZX Logical-X Memory Circuit: Distance-3 Validation

## Circuit configuration
- Code: Rotated XZZX surface code
- Distance: 3
- Data qubits: 9
- Syndrome ancillas: 8
- Measurement rounds: 3
- Logical qubits: 1

## Noiseless circuit validation
- Detector count: 24
- Observable count: 1
- Noiseless detector events: 0 in 1000 shots
- Noiseless logical flips: 0 in 1000 shots
- Detector error model generation: successful
- Noiseless error mechanisms: 0

## Algebraic stabilizer validation
- Stabilizer generators: 8
- Pairwise commutation: passed
- Binary symplectic rank: 8
- Stabilizer group size: 256
- Logical operator: X1 Z8 X15
- Logical operator commutes with all stabilizers: passed
- Logical operator outside stabilizer group: passed
- Minimum code distance: 3

## Code parameters

[[9, 1, 3]]

## Important scope limitation
The algebraic stabilizer validation establishes the intended
XZZX code space. Full circuit-level validation of the correspondence
between every measured ancilla and its stabilizer generator remains
a separate verification step.

No physical noise has been added yet. These results do not represent
a logical error-rate benchmark.
