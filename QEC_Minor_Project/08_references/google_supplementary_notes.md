Google Quantum AI — Supplementary Information Notes
Reference paper: Suppressing quantum errors by scaling a surface code logical qubit (2023)
Journal: Nature, 614, 676–681
DOI: 10.1038/s41586-022-05434-1

1. Table I — Average Probabilities of Main Errors
Experimental operation point
The table reports average probabilities of different error mechanisms at the experimental operation point of the distance-5 surface-code experiment.



Component
Error probability




Single-qubit (SQ) gates
(1.09 \times 10^{-3})


CZ gates
(6.05 \times 10^{-3})


Data-qubit idle
(2.46 \times 10^{-2})


Reset
(1.86 \times 10^{-3})


Readout
(1.96 \times 10^{-2})


CZ leakage
(2.0 \times 10^{-4})


Leakage from heating
(6.6 \times 10^{-4})


CZ crosstalk
(9.5 \times 10^{-4})



Important observations

Single-qubit gate errors are smaller than CZ gate errors.
Data-qubit idle errors are significant at the experimental operation point.
Readout errors are also substantial.
Leakage and crosstalk are additional error mechanisms.

Important distinction: The supplementary information states that the last three rows are not actual components of the surface-code circuit represented by the first five rows. They are included as additional reference effects for future analysis.
Relevance to our project
The first five probabilities provide an experimentally motivated reference for different circuit operations.
They must not be treated as universal transmon error probabilities.
We will initially exclude leakage and crosstalk from our simplified simulation.

2. Section V — Sensitivity of Logical Error per Cycle to Physical Errors
2.1 Objective
This section investigates how the logical error probability per cycle changes when the physical error probabilities of individual circuit components are varied.
The authors consider errors associated with:

Controlled-Z (CZ) gates.
Single-qubit (SQ) gates.
Data-qubit idle operations.
Readout.
Reset.
Leakage.
Crosstalk.

The purpose is to identify which physical error sources contribute most strongly to the logical error rate.
2.2 Simulation approach
The authors simulate the operation of a surface-code logical qubit using an error model corresponding to their experimental implementation.
For this analysis, they use:

Pauli+ simulation.
Correlated minimum-weight perfect matching for decoding.

The Pauli+ simulation incorporates additional physical effects beyond a simplified stochastic Pauli model.
2.3 Sensitivity coefficient
Let:
[
\epsilon = \text{Logical error probability per cycle}
]
and
[
p_{\mathrm{error}} = \text{Physical component error probability}
]
The sensitivity coefficient is defined as:
[
\boxed{
v_{\mathrm{error}} =
\frac{\partial \epsilon}
{\partial p_{\mathrm{error}}}
}
]
Here, the derivative represents how much the logical error probability changes when a particular component error probability changes.
The authors estimate this coefficient using linear regression of the simulated logical error probability against the corresponding physical component error probability.
2.4 Interpretation
A larger sensitivity coefficient indicates that the logical error probability is more sensitive to changes in that particular physical error source.
This analysis helps identify which hardware imperfections should be prioritised for improvement.
2.5 Relevance to our project
Our project will compare the standard rotated surface code and XZZX surface code.
The sensitivity analysis provides useful motivation for studying how different physical noise mechanisms affect logical performance.
We may later investigate how logical error rates respond to changes in individual noise components.

3. Section V.A — Experimental Operation Point
3.1 Purpose
This subsection describes the experimental operation point used to evaluate the sensitivity of the surface-code logical error rate to physical errors.
The authors consider variations in component error probabilities around the experimental operating conditions.
3.2 Component-specific error probabilities
The experimental operation point is based on the component probabilities reported in Table I.
The simulation distinguishes between different physical operations rather than assigning one common error probability to every operation.
The component-specific error probabilities are used to construct the error model.
3.3 Individual probabilities versus averages
The supplementary information notes that the simulator uses individual error probabilities for the corresponding components rather than simply assigning the mean probability to every component of the same type.
This distinction matters because physical qubits and operations can have different error characteristics.
3.4 Leakage considerations
The authors also discuss leakage as an additional source of error.
Two mechanisms are considered:

Leakage associated with CZ operations.
Leakage generated through non-equilibrium heating processes.

These effects are treated separately from the ordinary computational-subspace Pauli errors.
3.5 Relevance to our project
For our initial simulation:

We will use component-specific noise assumptions.
We will exclude leakage initially.
We will exclude crosstalk initially.
We will use a simplified stochastic Pauli representation.
We will clearly document the limitations of these approximations.

We will not claim to reproduce the complete Google experimental noise model.

4. Implications for Our MSc Project
The supplementary information establishes several useful principles for our modelling strategy.

Different circuit operations have different physical error probabilities.
Idle errors must be considered separately from gate errors.
Measurement and reset errors are distinct mechanisms.
Leakage and crosstalk are additional physical effects.
Logical performance depends on the combined effect of physical errors.
A simplified Pauli model is an approximation of the underlying physical noise.

Our initial modelling decisions



Item
Initial decision




Simulator
Stim


Decoder
PyMatching


Error representation
Stochastic Pauli channels


Leakage
Excluded


Crosstalk
Excluded


Coherent errors
Not modelled initially


Codes
Rotated surface and XZZX


Distances
3 and 5


Noise biases
1, 10 and 100


Primary metric
Logical error probability



Important methodological caution
The experimental component-error probabilities in Table I and the relaxation/dephasing probabilities derived from (T_1) and (T_2) are not interchangeable.
We must avoid double-counting physical errors if we combine these approaches.
Our primary model will be based on explicitly stated physical assumptions, with the experimental component-error table serving as a reference and potential comparison benchmark.

5. Source
Google Quantum AI, Suppressing quantum errors by scaling a surface code logical qubit, Nature 614, 676–681 (2023).
DOI: https://doi.org/10.1038/s41586-022-05434-1
Supplementary Information:

Table I: Average probabilities of main errors at the experimental operation point.
Section V: Sensitivity of logical error per cycle to physical errors.
Section V.A: Experimental operation point.

Note: These notes are a paraphrased research summary based on the supplementary-information material inspected. Consult the original PDF for exact definitions, equations and complete experimental details.
