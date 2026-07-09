import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(actual, expected, "Expected different output when calling 'calculate()' with '[0,1,2,3,4,5,6,7,8]'")

    def test_with_9_elements(self):
        actual = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[8.222222222222221, 0.6666666666666666, 10.666666666666666], [6.888888888888889, 10.666666666666666, 6.222222222222221], 7.987654320987654],
            'standard deviation': [[2.867441755680876, 0.816496580927726, 3.265986323710904], [2.6244998149106866, 3.265986323710904, 2.494438257849294], 2.8261730949018606],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [0, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        self.assertEqual(actual, expected, "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'")

    def test_with_less_than_9_elements(self):
        self.assertRaisesRegex(ValueError, "List must contain nine numbers.", mean_var_std.calculate, [2,6,4,8])

if __name__ == "__main__":
    unittest.main()
