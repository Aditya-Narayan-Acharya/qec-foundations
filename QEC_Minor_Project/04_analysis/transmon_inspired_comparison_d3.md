# Transmon-Inspired Noise Comparison

## Simulation configuration

- Code distance: 3
- Memory basis: Logical X
- T1: 20 microseconds
- Effective T2: 30 microseconds
- Effective interval: 921 ns
- Noise model: Pauli-twirled effective relaxation/dephasing channel
- Noise placement: Once before final data-qubit measurement
- Shots per code: 100,000
- Decoder: PyMatching
- Confidence intervals: 95% Wilson intervals

## Results

| Code | Logical failures | Logical error rate |
|---|---:|---:|
| Standard | 397 | 0.00397 |
| XZZX | 549 | 0.00549 |

The Standard surface code produced fewer logical failures than XZZX
under this particular effective transmon-inspired Pauli channel.

## Interpretation

The effective channel has larger X and Y probabilities than Z
probability. Therefore, it is not a Z-biased noise channel.

The result is consistent with the fact that XZZX's principal advantage
is associated with certain strongly biased noise regimes. It does not
establish that the Standard code is universally superior.

## Limitations

This is a simplified Pauli-twirled noise approximation based on
literature coherence parameters. The channel is applied once before
final data-qubit measurement.

It does not simulate decoherence continuously throughout syndrome
extraction. It also excludes explicit gate, readout, reset, leakage,
and crosstalk noise.

The result must not be described as a full circuit-level transmon
simulation or a threshold estimate.
