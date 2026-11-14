# Matched Biased Code-Capacity Benchmark

## Configuration
- Standard rotated surface code vs rotated XZZX surface code
- Distance: 3
- Logical memory: X
- Physical error probability: 0.01
- Noise bias: 10
- Shots per code: 100,000
- Noise: one independent biased Pauli error layer on data qubits
  immediately before final data measurement
- Decoder: PyMatching

## Physical error probabilities

- pX = 0.0008333333
- pY = 0.0008333333
- pZ = 0.0083333333

## Results

| Metric | Standard | XZZX |
|---|---:|---:|
| Detector events | 10614 | 6442 |
| Raw logical flips | 2689 | 1966 |
| Decoded logical failures | 125 | 63 |
| Logical error rate | 0.00125 | 0.00063 |
| 95% Wilson CI | [0.0010493, 0.0014890] | [0.0004925, 0.0008059] |

## Statistical comparison

Relative logical-error-rate reduction: 49.6%

Two-proportion z statistic: 4.5239

Two-sided p-value: 6.06985e-06

## Interpretation

At this operating point, the XZZX circuit produced a lower
decoded logical error rate than the standard surface-code circuit.

This is a single-distance, single-bias, single-physical-error-rate
code-capacity-style result. It is not a threshold estimate or a
full circuit-level transmon-noise benchmark.

Further validation of the transformed memory-X circuit's
stabilizer correspondence is required before making a general
claim about XZZX performance.
