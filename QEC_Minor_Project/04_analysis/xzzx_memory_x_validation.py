from itertools import product
import stim

DATA_QUBITS = [1, 3, 5, 8, 10, 12, 15, 17, 19]

STABILIZERS = [
    {1:"X", 3:"Z"},
    {1:"Z", 3:"X", 8:"X", 10:"Z"},
    {3:"Z", 5:"X", 10:"X", 12:"Z"},
    {5:"Z", 12:"X"},
    {8:"X", 15:"Z"},
    {8:"Z", 10:"X", 15:"X", 17:"Z"},
    {10:"Z", 12:"X", 17:"X", 19:"Z"},
    {17:"Z", 19:"X"}
]

def encode(pauli):
    xmask = 0
    zmask = 0
    for q, p in pauli.items():
        i = DATA_QUBITS.index(q)
        if p in ("X", "Y"):
            xmask |= 1 << i
        if p in ("Z", "Y"):
            zmask |= 1 << i
    return xmask | (zmask << 9)

def commutes(a, b):
    ax, az = a & 511, a >> 9
    bx, bz = b & 511, b >> 9
    return ((ax & bz).bit_count() + (az & bx).bit_count()) % 2 == 0

def binary_rank(vectors):
    basis = {}
    for v in vectors:
        while v:
            pivot = v.bit_length() - 1
            if pivot in basis:
                v ^= basis[pivot]
            else:
                basis[pivot] = v
                break
    return len(basis)

rows = [encode(s) for s in STABILIZERS]

assert all(
    commutes(rows[i], rows[j])
    for i in range(8) for j in range(i + 1, 8)
)

rank = binary_rank(rows)
assert rank == 8

stabilizer_group = {0}
for row in rows:
    stabilizer_group |= {x ^ row for x in list(stabilizer_group)}

logical_x = encode({1:"X", 8:"Z", 15:"X"})
assert all(commutes(logical_x, row) for row in rows)
assert logical_x not in stabilizer_group

minimum_distance = 10
for paulis in product(range(4), repeat=9):
    xmask = zmask = 0
    for i, p in enumerate(paulis):
        if p in (1, 3):
            xmask |= 1 << i
        if p in (2, 3):
            zmask |= 1 << i
    operator = xmask | (zmask << 9)
    if operator and operator not in stabilizer_group:
        if all(commutes(operator, row) for row in rows):
            weight = sum(p != 0 for p in paulis)
            minimum_distance = min(minimum_distance, weight)

assert minimum_distance == 3

print("XZZX algebraic validation passed")
print("Code parameters: [[9, 1, 3]]")
print("Stabilizer rank:", rank)
print("Minimum distance:", minimum_distance)
