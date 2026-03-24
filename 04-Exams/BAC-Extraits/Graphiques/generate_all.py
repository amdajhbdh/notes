#!/usr/bin/env python3
"""
Generate all remaining BAC graphs in batch
"""

import numpy as np
import matplotlib.pyplot as plt


def make_2020_graph():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect("equal")

    # Points from 2020
    A = 3 + 1j  # z_A = 3 + i
    B = 2j  # z_B = 2i
    C = 4 + 4j  # z_C = 4 + 4i
    D = A + C - B  # D = ABDC parallelogram

    ax.plot(A.real, A.imag, "ro", markersize=10)
    ax.plot(B.real, B.imag, "bo", markersize=10)
    ax.plot(C.real, C.imag, "go", markersize=10)
    ax.plot(D.real, D.imag, "mo", markersize=10)

    ax.annotate(
        "A(3+i)", xy=(A.real, A.imag), xytext=(A.real + 0.2, A.imag - 0.3), fontsize=10
    )
    ax.annotate(
        "B(2i)", xy=(B.real, B.imag), xytext=(B.real - 0.3, B.imag + 0.2), fontsize=10
    )
    ax.annotate(
        "C(4+4i)", xy=(C.real, C.imag), xytext=(C.real + 0.2, C.imag + 0.2), fontsize=10
    )
    ax.annotate(
        "D",
        xy=(D.real, D.imag),
        xytext=(D.real + 0.2, D.imag - 0.3),
        fontsize=10,
        color="purple",
    )

    ax.plot(
        [A.real, B.real, C.real, D.real, A.real],
        [A.imag, B.imag, C.imag, D.imag, A.imag],
        "purple",
        linewidth=1.5,
    )

    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.axvline(x=0, color="black", linewidth=0.8)
    ax.set_xlabel(r"$\Re(z)$", fontsize=14)
    ax.set_ylabel(r"$\Im(z)$", fontsize=14)
    ax.set_title("BAC 2020 D - Exercice 2: Plan complexe", fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 6)

    plt.tight_layout()
    plt.savefig(
        "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2020-D-Ex2.png",
        dpi=150,
    )
    print("Saved: BAC-2020-D-Ex2.png")
    plt.close()


def make_2019_D_graph():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect("equal")

    # Points from 2019
    A = -1 + 1j  # Sample points
    B = 2j
    C = 1 + 3j

    ax.plot(A.real, A.imag, "ro", markersize=10)
    ax.plot(B.real, B.imag, "bo", markersize=10)
    ax.plot(C.real, C.imag, "go", markersize=10)

    ax.annotate(
        "A", xy=(A.real, A.imag), xytext=(A.real - 0.3, A.imag - 0.3), fontsize=10
    )
    ax.annotate(
        "B", xy=(B.real, B.imag), xytext=(B.real + 0.2, B.imag + 0.2), fontsize=10
    )
    ax.annotate(
        "C", xy=(C.real, C.imag), xytext=(C.real + 0.2, C.imag + 0.2), fontsize=10
    )

    ax.plot([A.real, B.real, C.real], [A.imag, B.imag, C.imag], "purple", linewidth=1.5)

    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.axvline(x=0, color="black", linewidth=0.8)
    ax.set_xlabel(r"$\Re(z)$", fontsize=14)
    ax.set_ylabel(r"$\Im(z)$", fontsize=14)
    ax.set_title("BAC 2019 D - Plan complexe", fontsize=14)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(
        "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2019-D.png",
        dpi=150,
    )
    print("Saved: BAC-2019-D.png")
    plt.close()


def make_2018_D_graph():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect("equal")

    # Points from 2018 - typically rotations and transformations
    O = 0 + 0j
    A = 2 + 0j
    B = 0 + 2j

    ax.plot(A.real, A.imag, "ro", markersize=10)
    ax.plot(B.real, B.imag, "bo", markersize=10)
    ax.plot(O.real, O.imag, "ko", markersize=8)

    ax.annotate(
        "A(2)", xy=(A.real, A.imag), xytext=(A.real + 0.2, A.imag - 0.3), fontsize=10
    )
    ax.annotate(
        "B(2i)", xy=(B.real, B.imag), xytext=(B.real + 0.2, B.imag + 0.2), fontsize=10
    )
    ax.annotate("O", xy=(0, 0), xytext=(-0.5, -0.3), fontsize=10)

    # Draw angle arc
    theta = np.linspace(0, np.pi / 2, 50)
    ax.plot(np.cos(theta), np.sin(theta), "g--", linewidth=1)

    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.axvline(x=0, color="black", linewidth=0.8)
    ax.set_xlabel(r"$\Re(z)$", fontsize=14)
    ax.set_ylabel(r"$\Im(z)$", fontsize=14)
    ax.set_title("BAC 2018 D - Plan complexe (rotation)", fontsize=14)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(
        "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2018-D.png",
        dpi=150,
    )
    print("Saved: BAC-2018-D.png")
    plt.close()


def make_2022_D_Ex4_graph():
    """Exercice 4 from 2022 - f(x) = -(x+1)e^(-x) - 1"""
    fig, ax = plt.subplots(figsize=(12, 8))

    x = np.linspace(-4, 4, 1000)
    y = -(x + 1) * np.exp(-x) - 1

    ax.plot(x, y, "b-", linewidth=2, label=r"$\Gamma: f(x) = -(x+1)e^{-x} - 1$")
    ax.axhline(y=-1, color="red", linestyle="--", linewidth=1.5, label=r"$D: y = -1$")

    # Key points
    ax.plot(0, -1, "ro", markersize=8)
    ax.annotate(r"$(0, -1)$", xy=(0, -1), xytext=(0.5, -0.5), fontsize=11, color="red")
    ax.plot(-1, 0, "ro", markersize=8)
    ax.annotate(r"$(-1, 0)$", xy=(-1, 0), xytext=(-1.5, 0.5), fontsize=11, color="red")

    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.axvline(x=0, color="black", linewidth=0.5)
    ax.set_xlabel(r"$x$", fontsize=14)
    ax.set_ylabel(r"$y$", fontsize=14)
    ax.set_title("BAC 2022 D - Exercice 4: $f(x) = -(x+1)e^{-x} - 1$", fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=11)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 1)

    plt.tight_layout()
    plt.savefig(
        "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2022-D-Ex4.png",
        dpi=150,
    )
    print("Saved: BAC-2022-D-Ex4.png")
    plt.close()


# Run all
print("Generating all BAC graphs...")
make_2020_graph()
make_2019_D_graph()
make_2018_D_graph()
make_2022_D_Ex4_graph()
print("\nAll graphs generated!")
