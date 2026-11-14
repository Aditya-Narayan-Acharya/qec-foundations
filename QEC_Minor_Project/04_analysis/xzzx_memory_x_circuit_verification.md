# XZZX Distance-3 Circuit-Level Verification

## Circuit
- Rotated XZZX surface code
- Logical-X memory
- Distance: 3
- Data qubits: 9
- Syndrome ancillas: 8
- Measurement rounds: 3

## Derived stabilizer generators

| Ancilla | Measured stabilizer |
|---|---|
| 2 | X1 Z3 |
| 9 | Z1 X3 X8 Z10 |
| 11 | Z3 X5 X10 Z12 |
| 13 | Z5 X12 |
| 14 | X8 Z15 |
| 16 | Z8 X10 X15 Z17 |
| 18 | Z10 X12 X17 Z19 |
| 25 | Z17 X19 |

All eight generators were independently derived by backward
Pauli propagation through the circuit's Hadamard and CNOT gates.

All derived generators matched the expected XZZX stabilizers.

All eight ancillas had residual Z, consistent with computational-
basis ancilla preparation and measurement.

## Logical observable

The final measurement record corresponds to:

Xbar = X1 Z8 X15

The extracted logical observable matches the expected operator.

## Noiseless circuit checks

- Detectors: 24
- Observables: 1
- Detector events: 0 in 1000 shots
- Logical flips: 0 in 1000 shots
- Detector error model generation: successful

## Algebraic code validation

- Stabilizer generators: 8
- Stabilizer rank: 8
- Pairwise commutation: passed
- Logical qubits: 1
- Minimum code distance: 3
- Code parameters: [[9, 1, 3]]

## Conclusion

The distance-3 XZZX logical-X memory circuit passed the
noiseless, stabilizer-measurement, logical-observable and
algebraic code checks.

The circuit is suitable for the present code-capacity benchmark.
This verification does not establish full circuit-level
fault tolerance under noisy gates, measurements or resets.
