# XZZX Distance-3 Validation Report

## Circuit configuration

- Code: rotated XZZX surface code
- Distance: 3
- Syndrome rounds: 3
- Data qubits: 9
- Hadamard-transformed data qubits: [3, 8, 12, 17]

## Noiseless validation

- Shots: 1000
- Detector events: 0
- Logical flips: 0

## Stabilizer validation

- Stabilizer generators: 8
- Independent generators: 8
- Pairwise commutation: PASS
- Stabilizer group size: 256
- Encoded logical qubits: 1
- Calculated code distance: 3

## Transformed stabilizers

- Ancilla 2: X1 Z3
- Ancilla 9: Z1 X3 X8 Z10
- Ancilla 11: Z3 X5 X10 Z12
- Ancilla 13: Z5 X12
- Ancilla 14: X8 Z15
- Ancilla 16: Z8 X10 X15 Z17
- Ancilla 18: Z10 X12 X17 Z19
- Ancilla 25: Z17 X19

## Detector error model

- Detectors: 24
- Logical observables: 1
- Error mechanisms: 0
- PyMatching detector nodes: 24
- PyMatching logical observables: 1

Note: This circuit has no inserted physical noise. Zero error mechanisms
are expected. The decoder construction test does not yet validate noisy
decoding performance.

The stabilizer and distance calculations are algebraic checks derived
from the standard circuit's interaction pattern and the local Clifford
transformation. Full circuit-level noisy validation remains pending.
