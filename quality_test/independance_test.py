import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt
from scipy.special import erfc


def series_pair_test(observed_data, num_classes=10, alpha=0.01, is_print=False):
    # Générer des paires consécutives
    pairs = [(observed_data[i], observed_data[i + 1]) for i in range(0, len(observed_data) - 1, 2)]

    boxes = np.zeros((num_classes, num_classes))

    # Remplir les boîtes avec les occurrences observées
    for pair in pairs:
        box_x = int(pair[0] * num_classes)
        box_y = int(pair[1] * num_classes)
        boxes[box_x, box_y] += 1

    # Calculer les attentes théoriques si les nombres étaient complètement indépendants
    n = len(observed_data)
    expected_counts = (n / (2*num_classes**2)) * np.ones((num_classes, num_classes))

    # Calculer la statistique de test (chi carré)
    chi_squared_statistic = np.sum((boxes - expected_counts)**2 / expected_counts)

    # Déterminer le degré de liberté
    df = num_classes**2 - 1

    # Valeur critique du chi-carré à un certain niveau de signification
    chi_squared_critical = chi2.ppf(1 - alpha, df)

    if is_print: print(f"Q calculé : {round(chi_squared_statistic, 2)}, seuil critique {round(chi_squared_critical, 2)}")
    # x_coords, y_coords = zip(*pairs)
    # # Plot des résultats
    # plt.figure(figsize=(10, 6))
    # plt.scatter(x_coords, y_coords, color='red', marker='o', s=5)
    # plt.title('Distribution des paires en série')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.grid()
    # plt.xticks(np.arange(0, 1.1, 0.1))
    # plt.yticks(np.arange(0, 1.1, 0.1))
    # plt.show()

    return chi_squared_statistic < chi_squared_critical


def spectral_DFT_test(observed_data, alpha=0.01, is_print=False):
    # length of sequence
    n = len(observed_data)
    # transform 0 to -1
    observed_data = [2*o - 1 for o in observed_data]

    # calcul T
    T = np.sqrt(n*np.log(1/0.05))

    # calcul N0
    N0 = 0.95*n/2

    # Calcul FFT amplitude frequencies
    fft_result = np.fft.fft(observed_data)[:n//2]
    magnitude = np.abs(fft_result)

    #calcul N1
    N1 = sum(magnitude < T)

    # Calcul d
    d = (N1 - N0)/(np.sqrt(0.95*0.05*n/4))

    # calcul p-value
    p_value = erfc(abs(d)/np.sqrt(2))

    if is_print:
        # Tracer le spectre
        plt.figure(figsize=(10, 6))
        plt.plot(magnitude, label='Spectral Magnitude')
        plt.axhline(y=T, color='r', linestyle='--', label=f'Threshold at {round(T, 2)}')
        plt.title('Discrete Fourier Transform Test')
        plt.xlabel('Frequency')
        plt.ylabel('Magnitude')
        plt.legend()
        plt.show()

    return p_value > alpha


