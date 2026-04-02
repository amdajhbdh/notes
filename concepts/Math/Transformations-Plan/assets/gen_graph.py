import matplotlib.pyplot as plt
import numpy as np

def plot_transformation():
    # Points originaux (Carré ABCD)
    A = np.array([0, 0])
    B = np.array([10, 0])
    C = np.array([10, 10])
    D = np.array([0, 10])
    square = np.array([A, B, C, D, A])

    # Similitude de l'exercice 12: z' = (i/2)z + (5+5i)
    # En coordonnées: x' = -0.5y + 5, y' = 0.5x + 5
    def transform(p):
        return np.array([-0.5*p[1] + 5, 0.5*p[0] + 5])

    A_p = transform(A)
    B_p = transform(B)
    C_p = transform(C)
    D_p = transform(D)
    square_p = np.array([A_p, B_p, C_p, D_p, A_p])

    # Plot
    plt.figure(figsize=(8, 8))
    plt.plot(square[:, 0], square[:, 1], 'b-o', label='Original (Carré ABCD)')
    plt.plot(square_p[:, 0], square_p[:, 1], 'r-s', label='Image par Similitude s')
    
    # Centre Omega (2, 6)
    plt.plot(2, 6, 'gx', markersize=10, label='Centre Omega (2, 6)')
    
    plt.annotate('A', A)
    plt.annotate('B', B)
    plt.annotate('I = s(A)', A_p)
    plt.annotate('K = s(B)', B_p)
    
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.title('Visualisation de la Similitude Directe (Ex 12)\nAngle: +90°, Rapport: 0.5')
    plt.axis('equal')
    
    plt.savefig('01-Concepts/Math/Transformations-Plan/assets/similitude_ex12.png')
    plt.close()

if __name__ == "__main__":
    plot_transformation()
