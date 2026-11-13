
# Noise Model Module

## Completed

1. Literature parameter extraction.
2. Experimental component error documentation.
3. Energy relaxation model.
4. Initial noise-model assumptions.
5. Pauli probability calculator.

## Pauli noise model

Total error probability:

p = pX + pY + pZ

Noise bias:

eta = pZ / pX

Assumption:

pX = pY

Therefore:

pX = pY = p/(eta+2)

pZ = eta*p/(eta+2)

## Verification

Tested with:

p = 0.01

eta = 1, 10, 100

All probability sums and noise-bias
calculations verified successfully.

## Next milestone

Implement the noise model in Stim and
construct the first rotated surface-code
circuit.
