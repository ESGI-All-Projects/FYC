from datetime import datetime
import numpy as np
from tqdm import tqdm

def proportion_of_sequences_passing_a_test(PRNG, test, alpha, m, n, is_bit):
    gen = PRNG(seed=datetime.now().timestamp(), is_bit=is_bit)

    test_results = []
    for i in tqdm(range(m)):
        observed_data = []
        for j in range(n):
            observed_data.append(gen.next())
        test_results.append(test(observed_data, alpha=alpha))

    p = 1 - alpha
    IC = 3*np.sqrt((p*alpha)/m)
    proporsion_of_success = np.mean(test_results)

    test_succeded = p - IC < proporsion_of_success

    print(f"Proportion of success {round(proporsion_of_success,4)} has to be highter than {round(p - IC, 4)}")
    print(f"Test is {test_succeded}")


