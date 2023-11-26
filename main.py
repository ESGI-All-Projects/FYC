import random
from random import getrandbits
from datetime import datetime


from PRNG.linear_congruential_generator import LinearCongruentialGenerator
from PRNG.blum_blum_shub import BlumBlumShub
from PRNG.mersenne_twister import MersenneTwister
from quality_test.uniformity_test import chi2_test, kolmogorov_smirnov_test, frequency_monobit_test
from quality_test.independance_test import series_pair_test, spectral_DFT_test
from quality_test.test_protocol import proportion_of_sequences_passing_a_test




# # Test Chi2
# number_of_batch = 1000
# sample_size = 1000
# num_classes = 10
#
# # Mersenne twister
# print("Mersenne twister")
# list_chi2 = []
# mt = MersenneTwister(seed=datetime.now().timestamp())
# for i in range(number_of_batch):
#     # observed_data_mersenne_twister = [random.random() for _ in range(sample_size)]
#     # is_validated = chi2_test(observed_data_mersenne_twister, num_classes)
#     # list_chi2.append(is_validated)
#     observed_data_mersenne_twister = []
#     for _ in range(sample_size):
#         observed_data_mersenne_twister.append(mt.next())
#     is_validated = chi2_test(observed_data_mersenne_twister, num_classes)
#     list_chi2.append(is_validated)
# print(round(1 - sum(list_chi2)/number_of_batch, 3))

# list_chi2 = []
# for i in range(number_of_batch):
#     observed_data_mersenne_twister = [getrandbits(1) for _ in range(sample_size)]
#     is_validated = frequency_monobit_test(observed_data_mersenne_twister, alpha=0.01)
#     list_chi2.append(is_validated)
# print(round(sum(list_chi2)/number_of_batch, 3))
#
# # LCG
# print("LCG")
# list_chi2 = []
# lcg = LinearCongruentialGenerator(seed=datetime.now().timestamp())
# for i in range(number_of_batch):
#     observed_data_LCG = []
#     for _ in range(sample_size):
#         observed_data_LCG.append(lcg.next())
#     is_validated = chi2_test(observed_data_LCG, num_classes)
#     list_chi2.append(is_validated)
#     # print(is_validated)
# print(round(1 - sum(list_chi2)/number_of_batch, 3))

# lcg = MersenneTwister(seed=datetime.now().timestamp())
# observed_data_LCG = []
# for _ in range(10000):
#     observed_data_LCG.append(lcg.next())
# series_pair_test(observed_data_LCG)
#
# # Blum Blum Shub
# print("Blum Blum Shub")
# list_chi2 = []
# bbs = BlumBlumShub(seed=datetime.now().timestamp())
# for i in range(number_of_batch):
#     observed_data_BBS = []
#     for _ in range(sample_size):
#         observed_data_BBS.append(bbs.next())
#     is_validated = chi2_test(observed_data_BBS, num_classes)
#     list_chi2.append(is_validated)
#     # print(is_validated)
# print(round(1 - sum(list_chi2)/number_of_batch, 3))


def LCG_Mersenne_blum_test(test, n, alpha):
    test = test.lower()
    is_bit = True if test == "fm" else False

    # test2 = datetime.now().timestamp()
    mt = MersenneTwister(seed=datetime.now().timestamp(), is_bit=is_bit)
    lcg = LinearCongruentialGenerator(seed=datetime.now().timestamp(), is_bit=is_bit)
    bbs = BlumBlumShub(seed=datetime.now().timestamp(), is_bit=is_bit)

    # observed_data_mersenne_twister = [random.random() for _ in range(n)]
    observed_data_mersenne_twister = []
    observed_data_LCG = []
    observed_data_BBS = []

    for _ in range(n):
        observed_data_mersenne_twister.append(mt.next())
        observed_data_LCG.append(lcg.next())
        observed_data_BBS.append(bbs.next())

    if test == "chi2":
        print("Mersenne Twister")
        print(chi2_test(observed_data_mersenne_twister, 10, alpha=alpha, is_print=True))
        print("LCG")
        print(chi2_test(observed_data_LCG, 10, alpha=alpha, is_print=True))
        print("Blum blum shub")
        print(chi2_test(observed_data_BBS, 10, alpha=alpha, is_print=True))
    elif test == "ks":
        print("Mersenne Twister")
        print(kolmogorov_smirnov_test(observed_data_mersenne_twister, alpha=alpha, is_print=True))
        print("LCG")
        print(kolmogorov_smirnov_test(observed_data_LCG, alpha=alpha, is_print=True))
        print("Blum blum shub")
        print(kolmogorov_smirnov_test(observed_data_BBS, alpha=alpha, is_print=True))
    elif test == "fm":
        print("Mersenne Twister")
        print(frequency_monobit_test(observed_data_mersenne_twister, alpha=alpha, is_print=True))
        print("LCG")
        print(frequency_monobit_test(observed_data_LCG, alpha=alpha, is_print=True))
        print("Blum blum shub")
        print(frequency_monobit_test(observed_data_BBS, alpha=alpha, is_print=True))

# LCG_Mersenne_blum_test("ks", 1000, 0.05)

# proportion_of_sequences_passing_a_test(MersenneTwister, chi2_test, 0.01, 1000, 1000, False)
# proportion_of_sequences_passing_a_test(LinearCongruentialGenerator, chi2_test, 0.01, 1000, 1000, False)
# proportion_of_sequences_passing_a_test(BlumBlumShub, chi2_test, 0.01, 1000, 1000, False)

# proportion_of_sequences_passing_a_test(MersenneTwister, kolmogorov_smirnov_test, 0.01, 1000, 1000, False)
# proportion_of_sequences_passing_a_test(LinearCongruentialGenerator, kolmogorov_smirnov_test, 0.01, 1000, 1000, False)
# proportion_of_sequences_passing_a_test(BlumBlumShub, kolmogorov_smirnov_test, 0.01, 1000, 1000, False)

# proportion_of_sequences_passing_a_test(MersenneTwister, frequency_monobit_test, 0.01, 1000, 1000, True)
# proportion_of_sequences_passing_a_test(LinearCongruentialGenerator, frequency_monobit_test, 0.01, 1000, 1000, True)
# proportion_of_sequences_passing_a_test(BlumBlumShub, frequency_monobit_test, 0.01, 1000, 1000, True)

# proportion_of_sequences_passing_a_test(MersenneTwister, series_pair_test, 0.01, 1000, 1000, False)
# proportion_of_sequences_passing_a_test(LinearCongruentialGenerator, series_pair_test, 0.01, 1000, 1000, False)
# proportion_of_sequences_passing_a_test(BlumBlumShub, series_pair_test, 0.01, 1000, 1000, False)


proportion_of_sequences_passing_a_test(MersenneTwister, spectral_DFT_test, 0.01, 1000, 1000, True)
proportion_of_sequences_passing_a_test(LinearCongruentialGenerator, spectral_DFT_test, 0.01, 1000, 1000, True)
proportion_of_sequences_passing_a_test(BlumBlumShub, spectral_DFT_test, 0.01, 1000, 1000, True)