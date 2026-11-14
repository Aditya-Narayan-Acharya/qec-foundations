# Noise Model — Final Modelling Decisions

## 1. Experimental reference

Source: Google Quantum AI, Nature 614 (2023).

## 2. Physical reference parameters

- T1 = 20 microseconds
- T2_CPMG = 30 microseconds

T2_CPMG is a dynamical-decoupling coherence measurement.
It is not automatically equivalent to ordinary T2.

For our simplified phenomenological model, 30 microseconds
is used as an effective coherence parameter, denoted T2_eff.
It is not claimed to be an independently measured ordinary T2.

## 3. Experimental component probabilities

- Single-qubit gate: 1.09e-3
- CZ gate: 6.05e-3
- Data-qubit idle: 2.46e-2
- Reset: 1.86e-3
- Readout: 1.96e-2

These are experimental reference operation-point probabilities.
They are not directly combined with the T1/T2-derived channel.

## 4. Controlled biased Pauli model

Total Pauli error probability:

p = pX + pY + pZ

Noise bias:

eta = pZ / pX

The implemented model is:

pX = pY = p / (eta + 2)

pZ = eta * p / (eta + 2)

This guarantees:

pX + pY + pZ = p

and:

pZ / pX = eta

Noise biases used: eta = 1, 10, 100.

## 5. Effective transmon-inspired Pauli model

The simplified model uses:

T1 = 20 microseconds
T2_eff = 30 microseconds

For an interval t:

lambda1 = exp(-t/T1)
lambda2 = exp(-t/T2_eff)

The Pauli-twirled probabilities are:

pX = pY = (1 - lambda1)/4

pZ = (1 + lambda1 - 2*lambda2)/4

pI = 1 - pX - pY - pZ

The 921 ns interval is used to calculate the effective channel
for the final comparison.

This channel is applied once to the data qubits immediately
before final measurement. It is a simplified final-layer
decoherence proxy, not continuous noise during syndrome extraction.

## 6. Simulation architecture

- Simulator: Stim
- Decoder: PyMatching
- Codes: rotated Standard surface code and XZZX surface code
- Main comparison distance: d = 3

## 7. Excluded effects

- Explicit leakage
- Crosstalk
- Coherent errors
- Explicit gate-level relaxation and dephasing
- Continuous time-dependent noise during syndrome extraction

## 8. Scientific limitations

The controlled biased Pauli model and the transmon-inspired
Pauli-twirled model are separate modelling approaches.

The transmon-inspired model approximates coherence decay but
does not reproduce the non-unital nature of amplitude damping.

The final-layer comparison is not a full circuit-level transmon
simulation and does not establish a circuit-level threshold.
