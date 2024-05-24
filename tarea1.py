import unittest
from statistics import mean, pstdev

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def pstdev(numbers):
    if len(numbers) < 2:
        return 0
    mu = mean(numbers)
    variance = sum((x - mu) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

class TestStatistics(unittest.TestCase):
    def test_mean_empty_list(self):
        self.assertEqual(mean([]), 0)
    
    def test_mean_single_element(self):
        self.assertEqual(mean([5]), 5)
    
    def test_mean_positive_numbers(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)
    
    def test_mean_negative_numbers(self):
        self.assertEqual(mean([-1, -2, -3, -4, -5]), -3)
    
    def test_mean_mixed_numbers(self):
        self.assertEqual(mean([-1, 1, -2, 2, -3, 3]), 0)
    
    def test_stdev_empty_list(self):
        self.assertEqual(pstdev([]), 0)
    
    def test_stdev_single_element(self):
        self.assertEqual(pstdev([5]), 0)
    
    def test_stdev_positive_numbers(self):
        self.assertAlmostEqual(pstdev([1, 2, 3, 4, 5]), 1.4142135623730951)
    
    def test_stdev_negative_numbers(self):
        self.assertAlmostEqual(pstdev([-1, -2, -3, -4, -5]), 1.4142135623730951)
    
    def test_stdev_mixed_numbers(self):
        self.assertAlmostEqual(pstdev([-1, 1, -2, 2, -3, 3]), 2.160246899469287)

if __name__ == '__main__':
    unittest.main()
