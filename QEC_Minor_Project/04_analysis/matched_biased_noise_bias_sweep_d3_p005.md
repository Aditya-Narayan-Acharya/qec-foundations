# Matched Biased Noise-Bias Sweep

## Configuration

- Code distance: 3
- Memory basis: Logical X
- Physical error probability: 0.005
- Noise biases: [1, 10, 100]
- Shots per code per condition: 100000
- Noise model: Biased Pauli channel applied once before final data measurement
- Decoder: PyMatching
- Confidence intervals: 95% Wilson intervals

## Results

|   eta |   standard_pL |   xzzx_pL |   xzzx_reduction_percent |
|------:|--------------:|----------:|-------------------------:|
|     1 |       0.00018 |   0.00019 |                 -5.55556 |
|    10 |       0.00032 |   0.00022 |                 31.25    |
|   100 |       0.00037 |   9e-05   |                 75.6757  |

## Interpretation

At eta = 1, the two codes have nearly identical logical error rates.

At eta = 10, XZZX has a lower observed logical error rate.

At eta = 100, XZZX shows a substantially lower observed logical error rate
than the standard surface code.

The results are consistent with the expectation that XZZX can benefit
from strongly Z-biased noise. However, the statistical strength differs
between conditions, and the results are specific to distance 3.

## Limitations

This is a code-capacity-style benchmark with a single final data-noise
layer. It does not include noisy gates, repeated time-dependent noise,
ancilla faults, reset errors, or readout errors.

It is not a threshold estimate or a full circuit-level transmon simulation.
