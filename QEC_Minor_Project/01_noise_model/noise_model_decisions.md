
# Noise Model — Initial Decisions

## 1. Experimental reference

Source:
Google Quantum AI, Nature 614 (2023).

We use the reported experimental component
error probabilities as reference values.

## 2. Physical reference parameters

T1 = 20 microseconds
T2_CPMG = 30 microseconds

Ordinary T2 is not established from the
currently extracted reference information.

Therefore, T_phi will not be calculated
from T2_CPMG.

## 3. Experimental component probabilities

Single-qubit gate = 1.09e-3
CZ gate = 6.05e-3
Data-qubit idle = 2.46e-2
Reset = 1.86e-3
Readout = 1.96e-2

These values are reference operation-point
probabilities, not universal constants.

## 4. Controlled biased Pauli model

Total Pauli error probability:

p = pX + pY + pZ

Noise bias:

eta = pZ / pX

Initial assumption:

pX = pY = p / (2*(eta+1))

pZ = eta*p / (eta+1)

Noise biases:

eta = 1, 10, 100

This is a controlled modelling assumption.

## 5. Simulation architecture

Simulator: Stim
Decoder: PyMatching

Codes:
- Rotated standard surface code
- XZZX surface code

Distances:
- d = 3
- d = 5

## 6. Initially excluded effects

- Leakage
- Crosstalk
- Coherent errors
- Non-Pauli noise effects

## 7. Scientific limitations

The experimental component probabilities
and controlled biased Pauli model are
distinct modelling layers.

They must not be combined blindly.

Both codes must experience identical
physical noise assumptions during
each comparative simulation.
