import quiz_tests

import numpy as np
import scipy.stats as stats

def is_normal_ks(sample, test=stats.kstest, p_level=0.05, **kwargs):
    """
    sample: a sample distribution
    test: a function that tests for normality
    p_level: if the test returns a p-value > than p_level, assume normality

    return: True if distribution is normal, False otherwise
    """
    normal_args = (np.mean(sample), np.std(sample))

    t_stat, p_value = test(sample, 'norm', normal_args, **kwargs)
    print("Test statistic: {}, p-value: {}".format(t_stat, p_value))
    print("Is the distribution Likely Normal? {}".format(p_value > p_level))
    return p_value > p_level


quiz_tests.test_is_normal_ks(is_normal_ks)