# Effective Relaxation and Dephasing Model

## 1. Physical mechanism

Energy relaxation corresponds to:

|1> -> |0>

The reference relaxation time is:

T1 = 20 microseconds

## 2. Relaxation probability

For an interval t:

P_relax(t) = 1 - exp(-t/T1)

## 3. Effective coherence parameter

The reference reports T2_CPMG = 30 microseconds.

Because CPMG coherence is not automatically equivalent to
ordinary T2, we use this value only as an effective
phenomenological parameter:

T2_eff = 30 microseconds

We do not claim to have independently determined intrinsic T_phi.

## 4. Pauli-twirled approximation

Define:

lambda1 = exp(-t/T1)
lambda2 = exp(-t/T2_eff)

The effective Pauli probabilities are:

pX = pY = (1 - lambda1)/4

pZ = (1 + lambda1 - 2*lambda2)/4

pI = 1 - pX - pY - pZ

This approximation preserves the longitudinal and transverse
Bloch-vector decay factors of the effective model, but does not
preserve the non-unital translation of amplitude damping.

## 5. Effective probabilities for a 921 ns interval

For the final comparison:

- pX = 0.01125145
- pY = 0.01125145
- pZ = 0.00386532
- Total error probability = 0.02636822

## 6. Simulation implementation

The resulting Pauli channel is applied once to each data qubit
immediately before final data-qubit measurement.

This is a final-layer decoherence proxy. It is not a simulation
of continuous relaxation and dephasing throughout the syndrome-
extraction circuit.

## 7. Limitations

- The model is phenomenological.
- T2_CPMG is used as an effective coherence parameter.
- Pauli twirling removes non-unital amplitude-damping behaviour.
- Gate, measurement and reset errors are not explicitly added
  to this final comparison.
- This is not a full circuit-level transmon simulation.
