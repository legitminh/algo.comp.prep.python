import unittest

from twosat import two_sat


class TwoSatTests(unittest.TestCase):
    def test_returns_true_for_satisfiable_formula(self):
        clauses = [[1, 2], [-1, 2], [-1, -2], [1, -3]]

        self.assertTrue(two_sat(clauses))

    def test_returns_false_for_contradictory_formula(self):
        clauses = [[1, 1], [-1, -1]]

        self.assertFalse(two_sat(clauses))

    def test_handles_largest_variable_as_negative_literal(self):
        self.assertTrue(two_sat([[-3, 2]]))

    def test_empty_formula_is_satisfiable(self):
        self.assertTrue(two_sat([]))


if __name__ == "__main__":
    unittest.main()
