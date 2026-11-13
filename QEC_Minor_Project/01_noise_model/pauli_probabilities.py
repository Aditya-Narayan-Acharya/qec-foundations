
def calculate_pauli_probabilities(p, eta):
    """
    Calculate X, Y and Z Pauli error probabilities.

    p   : Total Pauli error probability
    eta : Noise bias = pZ / pX

    Assumption: pX = pY
    """

    if not 0 <= p <= 1:
        raise ValueError("p must be between 0 and 1")

    if eta <= 0:
        raise ValueError("eta must be positive")

    p_x = p / (eta + 2)
    p_y = p / (eta + 2)
    p_z = eta * p / (eta + 2)

    return p_x, p_y, p_z


# Test parameters
physical_error_rate = 0.01
noise_biases = [1, 10, 100]

print("Total physical error rate:", physical_error_rate)
print()

for eta in noise_biases:

    px, py, pz = calculate_pauli_probabilities(
        physical_error_rate, eta
    )

    print(f"Noise bias = {eta}")
    print(f"pX = {px:.8f}")
    print(f"pY = {py:.8f}")
    print(f"pZ = {pz:.8f}")

    print("Probability sum:", px + py + pz)
    print("Verified bias:", pz / px)
    print("-" * 35)
