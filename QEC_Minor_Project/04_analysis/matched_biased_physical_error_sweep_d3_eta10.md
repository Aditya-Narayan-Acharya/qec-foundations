# Matched Biased Physical-Error-Rate Sweep

## Configuration

- Code distance: 3
- Memory basis: Logical X
- Noise model: Biased Pauli channel applied once before final data measurement
- Noise bias: eta = 10
- Physical error rates: [0.001, 0.002, 0.003, 0.005, 0.01]
- Shots per code per point: 100000
- Decoder: PyMatching
- Confidence intervals: 95% Wilson intervals

## Results

|     p |   standard_pL |   xzzx_pL |   xzzx_reduction_percent |
|------:|--------------:|----------:|-------------------------:|
| 0.001 |       1e-05   |   1e-05   |                   0      |
| 0.002 |       2e-05   |   2e-05   |                   0      |
| 0.003 |       0.00018 |   4e-05   |                  77.7778 |
| 0.005 |       0.00043 |   0.00019 |                  55.814  |
| 0.01  |       0.00145 |   0.0006  |                  58.6207 |

## Interpretation

At p = 0.001 and p = 0.002, both codes produced very few logical failures.
These low event counts do not establish a meaningful performance difference.

At the three higher physical error rates, XZZX produced fewer decoded
logical failures than the standard surface code in this simulation.

The results are preliminary and specific to distance 3, the chosen logical-X
memory circuits, eta = 10, and the final-data-measurement noise model.

This is a code-capacity-style benchmark. It does not include repeated
time-dependent noise accumulation, noisy gates, ancilla faults, reset
errors, or readout errors. It is not a threshold estimate and should not
be described as a full circuit-level transmon simulation.

## Files

- Numerical results: matched_biased_physical_error_sweep_d3_eta10.csv
- Comparison graph: matched_biased_physical_error_sweep_d3_eta10.png
