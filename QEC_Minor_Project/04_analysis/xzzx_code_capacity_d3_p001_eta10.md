# XZZX Distance-3 Biased Pauli Noise Experiment

## Configuration

- Code: XZZX surface code
- Distance: 3
- Noise model: one biased Pauli error layer before final data measurements
- Physical error rate: 0.01
- Noise bias: 10
- Shots: 100000
- Random seed: 20261115

## Pauli probabilities

- pX: 0.0008333333
- pY: 0.0008333333
- pZ: 0.0083333333

## Results

- Detection events: 6335
- Raw logical observable flips: 1202
- Logical failures after decoding: 45
- Logical error rate: 0.00045000
- 95% Wilson confidence interval: [0.00033635, 0.00060203]
- Detector error mechanisms: 7

## Interpretation

This is a controlled single-layer data-noise experiment.
It is not a full circuit-level transmon noise simulation.
It is one parameter point, not a threshold measurement or
evidence by itself of superiority over the standard surface code.

## Reproducibility

The simulation code is stored in
`03_simulations/scripts/xzzx_code_capacity_d3.py`.

The results are stored in
`03_simulations/results/xzzx_code_capacity_d3_p001_eta10.csv`.
