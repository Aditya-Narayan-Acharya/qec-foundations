
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def wilson_interval(failures, shots, z=1.96):
    """Calculate 95% Wilson confidence intervals."""
    k = np.asarray(failures, dtype=float)
    n = np.asarray(shots, dtype=float)

    p = k / n
    denominator = 1 + z**2 / n

    centre = (p + z**2 / (2*n)) / denominator
    half_width = (
        z * np.sqrt(
            p*(1-p)/n + z**2/(4*n**2)
        ) / denominator
    )

    return centre - half_width, centre + half_width


def plot_logical_error_rate(
    csv_file,
    output_name="logical_error_rate",
    code_label="Rotated surface code, distance 3"
):
    data = pd.read_csv(csv_file)
    data = data.sort_values("physical_noise_parameter")

    p = data["physical_noise_parameter"].to_numpy()
    pL = data["logical_error_rate"].to_numpy()

    lower, upper = wilson_interval(
        data["failures"],
        data["shots"]
    )

    errors = np.vstack([
        pL - lower,
        upper - pL
    ])

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.labelsize": 13,
        "axes.titlesize": 15,
        "legend.fontsize": 10,
        "axes.linewidth": 1.0,
        "savefig.facecolor": "white",
        "figure.facecolor": "white"
    })

    fig, ax = plt.subplots(
        figsize=(8, 5.5),
        constrained_layout=True
    )

    ax.errorbar(
        p,
        pL,
        yerr=errors,
        marker="o",
        markersize=7,
        linewidth=2,
        capsize=4,
        label=code_label
    )

    ax.set_xscale("log")
    ax.set_yscale("log")

    ax.set_xlabel(r"Physical noise parameter, $p$")
    ax.set_ylabel(r"Logical error probability, $p_L$")

    ax.set_title("Logical Error Rate vs Physical Noise")

    ax.grid(
        True,
        which="major",
        linewidth=0.7,
        alpha=0.35
    )

    ax.grid(
        True,
        which="minor",
        linewidth=0.4,
        alpha=0.18
    )

    ax.legend(frameon=False, loc="upper left")

    ax.text(
        0.98,
        0.04,
        f"{int(data['shots'].iloc[0]):,} shots per point\n"
        "95% Wilson confidence intervals",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=8.5
    )

    output_dir = Path(
        "/content/qec-foundations/QEC_Minor_Project/"
        "03_simulations/graphs"
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    base = output_dir / output_name

    fig.savefig(
        base.with_suffix(".png"),
        dpi=400,
        bbox_inches="tight"
    )

    fig.savefig(
        base.with_suffix(".pdf"),
        bbox_inches="tight"
    )

    fig.savefig(
        base.with_suffix(".svg"),
        bbox_inches="tight"
    )

    plt.show()
    plt.close(fig)

    print("Graph files saved:")
    print(base.with_suffix(".png"))
    print(base.with_suffix(".pdf"))
    print(base.with_suffix(".svg"))
