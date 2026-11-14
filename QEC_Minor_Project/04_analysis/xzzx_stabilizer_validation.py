import stim
import numpy as np
import pymatching
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]

CIRCUITS_DIR = PROJECT_DIR / "02_circuits"
ANALYSIS_DIR = PROJECT_DIR / "04_analysis"

CIRCUITS_DIR.mkdir(parents=True, exist_ok=True)

distance = 3
rounds = 3

# 1. Generate standard circuit
standard = stim.Circuit.generated(
    "surface_code:rotated_memory_z",
    distance=distance,
    rounds=rounds
).flattened()

# 2. Identify coordinates and data qubits
coordinates = {}

for instruction in standard:
    if instruction.name == "QUBIT_COORDS":
        q = instruction.targets_copy()[0].value
        coordinates[q] = instruction.gate_args_copy()

data_qubits = sorted({
    target.value
    for instruction in standard
    if instruction.name == "M"
    for target in instruction.targets_copy()
})

ancilla_qubits = sorted(set(coordinates) - set(data_qubits))

# 3. Checkerboard Hadamard selection
selected_data = {
    q for q in data_qubits
    if (
        int((coordinates[q][0] - 1) / 2)
        + int((coordinates[q][1] - 1) / 2)
    ) % 2 == 1
}

assert selected_data == {3, 8, 12, 17}

# 4. Construct locally Clifford-transformed circuit
xzzx = stim.Circuit()

for instruction in standard:
    name = instruction.name
    targets = instruction.targets_copy()

    if name == "R":
        for target in targets:
            q = target.value
            xzzx.append("RX" if q in selected_data else "R", [q])

    elif name == "M":
        for target in targets:
            q = target.value
            xzzx.append("MX" if q in selected_data else "M", [q])

    elif name == "CX":
        affected = sorted({
            target.value
            for target in targets
            if target.value in selected_data
        })

        if affected:
            xzzx.append("H", affected)

        xzzx.append(instruction)

        if affected:
            xzzx.append("H", affected)

    else:
        xzzx.append(instruction)

# Save both circuits
(CIRCUITS_DIR / "standard_surface_code_d3.stim").write_text(str(standard))
(CIRCUITS_DIR / "xzzx_surface_code_d3.stim").write_text(str(xzzx))

# 5. Noiseless validation
sampler = xzzx.compile_detector_sampler(seed=1234)

detectors, observables = sampler.sample(
    shots=1000,
    separate_observables=True
)

assert not np.any(detectors)
assert not np.any(observables)

# 6. Extract standard stabilizers
stabilizers = {}

for instruction in standard:
    if instruction.name != "CX":
        continue

    targets = instruction.targets_copy()

    for i in range(0, len(targets), 2):
        control = targets[i].value
        target = targets[i + 1].value

        if control in ancilla_qubits and target in data_qubits:
            ancilla, data, stype = control, target, "X"

        elif control in data_qubits and target in ancilla_qubits:
            ancilla, data, stype = target, control, "Z"

        else:
            continue

        if ancilla not in stabilizers:
            stabilizers[ancilla] = {
                "type": stype,
                "data": set()
            }

        assert stabilizers[ancilla]["type"] == stype
        stabilizers[ancilla]["data"].add(data)

# 7. Transform stabilizers
transformed = {}

for ancilla, stabilizer in stabilizers.items():
    original_type = stabilizer["type"]
    transformed[ancilla] = {}

    for q in sorted(stabilizer["data"]):
        if original_type == "X":
            pauli = "Z" if q in selected_data else "X"
        else:
            pauli = "X" if q in selected_data else "Z"

        transformed[ancilla][q] = pauli

# 8. Pairwise commutation
def commute(s1, s2):
    count = sum(
        s1[q] != s2[q]
        for q in set(s1) & set(s2)
    )
    return count % 2 == 0

ancillas = sorted(transformed)

for i in range(len(ancillas)):
    for j in range(i + 1, len(ancillas)):
        assert commute(
            transformed[ancillas[i]],
            transformed[ancillas[j]]
        )

# 9. Binary symplectic representation
n = len(data_qubits)
rows = []

for ancilla in ancillas:
    x_bits = 0
    z_bits = 0

    for q, pauli in transformed[ancilla].items():
        index = data_qubits.index(q)

        if pauli in ("X", "Y"):
            x_bits |= 1 << index

        if pauli in ("Z", "Y"):
            z_bits |= 1 << index

    rows.append(x_bits | (z_bits << n))

def gf2_rank(input_rows):
    matrix = input_rows.copy()
    rank = 0

    for col in range(2 * n):
        pivot = next(
            (i for i in range(rank, len(matrix))
             if (matrix[i] >> col) & 1),
            None
        )

        if pivot is None:
            continue

        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]

        for i in range(len(matrix)):
            if i != rank and ((matrix[i] >> col) & 1):
                matrix[i] ^= matrix[rank]

        rank += 1

    return rank

rank = gf2_rank(rows)
k = n - rank

assert rank == 8
assert k == 1

# 10. Generate stabilizer group
stabilizer_group = {0}

for row in rows:
    stabilizer_group |= {
        element ^ row for element in stabilizer_group
    }

assert len(stabilizer_group) == 2 ** rank

# 11. Exhaustive logical distance search
logical_distance = float("inf")
logical_operator = None
mask = (1 << n) - 1

for operator in range(1, 1 << (2 * n)):
    x_op = operator & mask
    z_op = operator >> n

    commutes_with_all = True

    for row in rows:
        x_stab = row & mask
        z_stab = row >> n

        parity = (
            (x_op & z_stab).bit_count()
            + (z_op & x_stab).bit_count()
        ) % 2

        if parity:
            commutes_with_all = False
            break

    if not commutes_with_all:
        continue

    if operator in stabilizer_group:
        continue

    weight = (x_op | z_op).bit_count()

    if weight < logical_distance:
        logical_distance = weight
        logical_operator = operator

assert logical_distance == 3

# 12. Construct detector error model and decoder
dem = xzzx.detector_error_model(decompose_errors=True)

matching = pymatching.Matching.from_detector_error_model(dem)

error_mechanisms = sum(
    instruction.type == "error"
    for instruction in dem
)

# 13. Generate validation report
stabilizer_lines = []

for ancilla in ancillas:
    terms = " ".join(
        f"{pauli}{q}"
        for q, pauli in transformed[ancilla].items()
    )
    stabilizer_lines.append(f"- Ancilla {ancilla}: {terms}")

report = f"""# XZZX Distance-3 Validation Report

## Circuit configuration

- Code: rotated XZZX surface code
- Distance: {distance}
- Syndrome rounds: {rounds}
- Data qubits: {n}
- Hadamard-transformed data qubits: {sorted(selected_data)}

## Noiseless validation

- Shots: 1000
- Detector events: {int(np.sum(detectors))}
- Logical flips: {int(np.sum(observables))}

## Stabilizer validation

- Stabilizer generators: {len(rows)}
- Independent generators: {rank}
- Pairwise commutation: PASS
- Stabilizer group size: {len(stabilizer_group)}
- Encoded logical qubits: {k}
- Calculated code distance: {logical_distance}

## Transformed stabilizers

{chr(10).join(stabilizer_lines)}

## Detector error model

- Detectors: {xzzx.num_detectors}
- Logical observables: {xzzx.num_observables}
- Error mechanisms: {error_mechanisms}
- PyMatching detector nodes: {matching.num_detectors}
- PyMatching logical observables: {matching.num_fault_ids}

Note: This circuit has no inserted physical noise. Zero error mechanisms
are expected. The decoder construction test does not yet validate noisy
decoding performance.

The stabilizer and distance calculations are algebraic checks derived
from the standard circuit's interaction pattern and the local Clifford
transformation. Full circuit-level noisy validation remains pending.
"""

report_file = ANALYSIS_DIR / "xzzx_validation_report.md"
report_file.write_text(report)

print("XZZX VALIDATION SCRIPT COMPLETED")
print("=" * 50)
print("Data qubits:", n)
print("Selected data qubits:", sorted(selected_data))
print("Independent stabilizers:", rank)
print("Encoded logical qubits:", k)
print("Code distance:", logical_distance)
print("Noiseless detector events:", int(np.sum(detectors)))
print("Noiseless logical flips:", int(np.sum(observables)))
print("Detector error mechanisms:", error_mechanisms)
print("PyMatching decoder: constructed")
print("\nSaved validation report:", report_file)
