from pathlib import Path
import csv
import numpy as np
import stim
import pymatching

PROJECT = Path(__file__).resolve().parents[2]

circuit_file = PROJECT / "02_circuits/xzzx_surface_code_d3.stim"

p = 0.01
eta = 10
shots = 100_000
seed = 20261115

circuit = stim.Circuit.from_file(str(circuit_file))

data_qubits = sorted({
    target.value
    for instruction in circuit
    if instruction.name in ["M", "MX"]
    for target in instruction.targets_copy()
})

pX = p / (eta + 2)
pY = p / (eta + 2)
pZ = eta * p / (eta + 2)

# Add one biased Pauli error layer before final data measurements.
noisy_circuit = stim.Circuit()

for instruction in circuit:

    if instruction.name in ["M", "MX"]:
        for target in instruction.targets_copy():
            q = target.value

            if q in data_qubits:
                noisy_circuit.append(
                    "PAULI_CHANNEL_1",
                    [q],
                    [pX, pY, pZ]
                )

    noisy_circuit.append(instruction)

dem = noisy_circuit.detector_error_model(
    decompose_errors=True
)

matching = pymatching.Matching.from_detector_error_model(dem)

sampler = noisy_circuit.compile_detector_sampler(seed=seed)

detectors, actual_observables = sampler.sample(
    shots=shots,
    separate_observables=True
)

predicted_observables = np.asarray(
    matching.decode_batch(detectors)
)

if predicted_observables.ndim == 1:
    predicted_observables = predicted_observables.reshape(-1, 1)

failures = np.any(
    predicted_observables != actual_observables,
    axis=1
)

logical_failures = int(np.sum(failures))
raw_flips = int(np.sum(actual_observables))

pl = logical_failures / shots

# 95% Wilson confidence interval
z = 1.96
den = 1 + z**2 / shots

center = (pl + z**2 / (2 * shots)) / den

half = (
    z * np.sqrt(
        pl * (1 - pl) / shots
        + z**2 / (4 * shots**2)
    ) / den
)

lower = center - half
upper = center + half

error_mechanisms = sum(
    instruction.type == "error"
    for instruction in dem
)

result = {
    "code": "XZZX",
    "distance": 3,
    "noise_model": "Single final data-error layer",
    "physical_error_rate": p,
    "noise_bias": eta,
    "pX": pX,
    "pY": pY,
    "pZ": pZ,
    "shots": shots,
    "seed": seed,
    "detection_events": int(np.sum(detectors)),
    "raw_logical_flips": raw_flips,
    "logical_failures_after_decoding": logical_failures,
    "logical_error_rate": pl,
    "wilson_95_lower": lower,
    "wilson_95_upper": upper,
    "detector_error_mechanisms": error_mechanisms
}

results_dir = PROJECT / "03_simulations/results"
analysis_dir = PROJECT / "04_analysis"

csv_file = results_dir / "xzzx_code_capacity_d3_p001_eta10.csv"

with csv_file.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=result.keys())
    writer.writeheader()
    writer.writerow(result)

report = f"""# XZZX Distance-3 Biased Pauli Noise Experiment

## Configuration

- Code: XZZX surface code
- Distance: 3
- Noise model: one biased Pauli error layer before final data measurements
- Physical error rate: {p}
- Noise bias: {eta}
- Shots: {shots}
- Random seed: {seed}

## Pauli probabilities

- pX: {pX:.10f}
- pY: {pY:.10f}
- pZ: {pZ:.10f}

## Results

- Detection events: {result['detection_events']}
- Raw logical observable flips: {raw_flips}
- Logical failures after decoding: {logical_failures}
- Logical error rate: {pl:.8f}
- 95% Wilson confidence interval: [{lower:.8f}, {upper:.8f}]
- Detector error mechanisms: {error_mechanisms}

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
"""

report_file = analysis_dir / "xzzx_code_capacity_d3_p001_eta10.md"
report_file.write_text(report)

print("EXPERIMENT SAVED")
print("=" * 50)
print("Logical failures:", logical_failures)
print(f"Logical error rate: {pl:.8f}")
print(f"95% CI: [{lower:.8f}, {upper:.8f}]")
print("\nCSV:", csv_file)
print("Report:", report_file)
