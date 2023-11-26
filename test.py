import numpy as np
import matplotlib.pyplot as plt


def generate_random_sequence(prng, length):
    """Générer une séquence de nombres aléatoires avec le PRNG spécifié."""
    sequence = []
    for _ in range(length):
        sequence.append(prng())
    return np.array(sequence)


def spectral_test(sequence):
    """Effectuer le test spectral des hyperplans sur la séquence donnée."""
    n = len(sequence)
    bits = np.array(sequence)

    # Générer une matrice de Hadamard de dimension n
    hadamard_matrix = np.fft.fft(np.eye(n)) / np.sqrt(n)

    # Transformer la séquence en espace de fréquence
    spectrum = np.abs(np.fft.fft(bits))

    # Calculer le produit scalaire entre le spectre et chaque ligne de la matrice de Hadamard
    dot_products = np.abs(np.dot(hadamard_matrix, spectrum))

    # Tracer le résultat du test spectral
    plt.plot(dot_products)
    plt.title("Test spectral des hyperplans")
    plt.xlabel("Ligne de la matrice de Hadamard")
    plt.ylabel("Produit scalaire avec le spectre")
    plt.show()


# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez la fonction suivante par votre propre PRNG
    def my_prng():
        return np.random.randint(2)


    # Longueur de la séquence à tester
    sequence_length = 1024

    # Générer une séquence avec le PRNG
    random_sequence = generate_random_sequence(my_prng, sequence_length)

    # Effectuer le test spectral des hyperplans
    spectral_test(random_sequence)
