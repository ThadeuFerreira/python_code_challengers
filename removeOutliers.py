import numpy as np
import unittest
from unittest import TestCase
np.set_printoptions(precision = 2)
def clean_mean(sample, cutoff):
    sample = np.array(sample)
    std = np.std(sample)
    mean = np.mean(sample)
    outliers = np.abs(sample - mean) > cutoff * std
    while outliers.any():
        sample = sample[~outliers]
        std = np.std(sample)
        mean = np.mean(sample)
        outliers = np.abs(sample - mean) > cutoff * std
    return np.mean(sample)


class Test(TestCase):
    def test_example(self):
        " Example test case "
        sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
        cutoff = 3
        self.assertAlmostEqual(clean_mean(sample, cutoff), 5.5)

#run the tests
if __name__ == "__main__":
    unittest.main()
