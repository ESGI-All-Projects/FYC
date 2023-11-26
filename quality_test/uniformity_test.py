import numpy as np
from scipy.stats import chi2, kstwobign
from scipy.special import erfc

def chi2_test(observed_data, num_classes=10, alpha=0.01, is_print=False):
    hist, bin_edges = np.histogram(observed_data, bins=num_classes)

    # Calcul des fréquences attendues (une distribution uniforme est attendue)
    total_observations = len(observed_data)
    expected_frequency = total_observations / num_classes

    # Calcul de la statistique du chi-carré
    chi_squared_statistic = sum([(observed - expected_frequency) ** 2 / expected_frequency for observed in hist])

    # Degré de liberté (nombre de classes - 1)
    df = num_classes - 1

    # Valeur critique du chi-carré à un certain niveau de signification
    chi_squared_critical = chi2.ppf(1 - alpha, df)

    # p-value
    p_value = 1 - chi2.cdf(chi_squared_statistic, df)


    if is_print: print(f"Q calculé : {round(chi_squared_statistic, 2)}, seuil critique {round(chi_squared_critical,2 )}\nP-value : {p_value}")

    return chi_squared_statistic < chi_squared_critical


def kolmogorov_smirnov_test(observed_data, alpha=0.01, is_print=False):
    """
    Effectue le test de Kolmogorov-Smirnov pour un échantillon par rapport à une distribution uniforme.

    :param sample: Échantillon de données
    :return: Statistique de test KS, p-valeur
    """

    # Trier l'échantillon
    observed_data = sorted(observed_data)

    # Taille de l'échantillon
    n = len(observed_data)

    # Calculate max(i/N-Ri)
    K_plus = list()
    for i in range(1, n + 1):
        diff = i / n - observed_data[i - 1]
        K_plus.append(diff)
    K_plus_max = np.sqrt(n) * np.max(K_plus)

    # Calculate max(Ri-((i-1)/N))
    K_minus = list()
    for i in range(1, n + 1):
        diff = observed_data[i - 1] - (i - 1) / n
        K_minus.append(diff)
    K_minus_max = np.sqrt(n) * np.max(K_minus)

    # Calculate KS Statistic
    K_max = max(K_plus_max, K_minus_max)

    critical_value = kstwobign.ppf(1 - alpha)

    # p-value
    p_value = 1 - kstwobign.cdf(K_max)

    if is_print: print(f"K calculé : {round(K_max, 2)}, seuil critique {round(critical_value,2 )}\nP-value : {p_value}")

    return K_max < critical_value


def frequency_monobit_test(observed_data, alpha=0.01, is_print=False):
    n = len(observed_data)
    observed_data = [2*o - 1 for o in observed_data]
    S = abs(sum(observed_data))/np.sqrt(n)

    p_value = erfc(S/np.sqrt(2))
    return p_value > alpha
