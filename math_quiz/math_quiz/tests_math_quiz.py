import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random integers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the valid operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, valid_operators)

    def test_calculate_result_addition(self):
        result = calculate_result(5, 2, '+')
        self.assertEqual(result, 7)

    def test_calculate_result_subtraction(self):
        result = calculate_result(5, 2, '-')
        self.assertEqual(result, 3)

    def test_calculate_result_multiplication(self):
        result = calculate_result(5, 2, '*')
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
