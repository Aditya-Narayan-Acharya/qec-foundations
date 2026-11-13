
# Energy Relaxation Model

## Physical mechanism

Energy relaxation is the transition:

|1> -> |0>

## Experimental parameter

T1 = 20 microseconds

## Mathematical model

P_relax(t) = 1 - exp(-t/T1)

## Calculated probabilities

| Operation | Duration (ns) | P_relax |
|---|---:|---:|
| Single-qubit gate | 25 | 0.001249 |
| CZ gate | 34 | 0.001699 |
| Measurement | 500 | 0.024690 |
| Reset interval | 160 | 0.007968 |

## Interpretation

Relaxation probability increases with
the duration of exposure to energy relaxation.

These values represent the relaxation
contribution only, not total operation errors.

## Modelling limitation

Stim's stochastic Pauli representation
does not preserve the non-unital nature
of amplitude damping exactly.

A Pauli-twirled approximation may be used
for the initial simulation.
