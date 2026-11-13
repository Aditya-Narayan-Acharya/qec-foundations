
# Literature-Derived Transmon Parameters

## Reference paper

Google Quantum AI (2023).

"Suppressing quantum errors by scaling a surface code logical qubit."

Nature, 614, 676–681.

DOI: 10.1038/s41586-022-05434-1

## 1. Physical device parameters

| Parameter | Value | Unit |
|---|---:|---|
| T1 | 20 | microseconds |
| T2_CPMG | 30 | microseconds |
| Single-qubit gate duration | 25 | ns |
| CZ gate duration | 34 | ns |
| Measurement duration | 500 | ns |
| Reset duration | 160 | ns |

Note: T2_CPMG is a dynamical-decoupling coherence
measurement. It must not automatically be treated
as ordinary T2.

## 2. Experimental component error probabilities

| Component | Error probability |
|---|---:|
| Single-qubit gates | 1.09e-3 |
| CZ gates | 6.05e-3 |
| Data-qubit idle | 2.46e-2 |
| Reset | 1.86e-3 |
| Readout | 1.96e-2 |

These values correspond to the experimental
operation point of the distance-5 surface-code
experiment.

They are not universal transmon error rates.

## 3. Additional error sources

| Error source | Probability |
|---|---:|
| CZ leakage | 2.0e-4 |
| Leakage from heating | 6.6e-4 |
| CZ crosstalk | 9.5e-4 |

These will initially be excluded from our
simplified simulation model.

## 4. Initial modelling decisions

- Simulator: Stim
- Decoder: PyMatching
- Error representation: stochastic Pauli channels
- Leakage: excluded initially
- Crosstalk: excluded initially
- Coherent errors: excluded initially
- Codes: rotated surface code and XZZX
- Code distances: 3 and 5
- Noise biases: 1, 10 and 100

## 5. Important limitations

1. The reported T2 value is T2_CPMG.
2. We cannot directly calculate T_phi using
   T2_CPMG without further justification.
3. Experimental component error probabilities
   are not identical to T1/T2-derived probabilities.
4. Noise bias will be introduced as a separate
   controlled modelling assumption.
5. Our simulation will be a simplified model,
   not an exact reproduction of Google's experiment.
