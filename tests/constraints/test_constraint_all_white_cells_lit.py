import unittest
from functions.constraints.check_constraint_all_white_cells_lit import check_constraint_all_white_cells_lit


class TestConstraintAllWhiteCellsLit(unittest.TestCase):
    def test_valid(self):
        """
            ✅ Test pozytywny: Wszystkie pola są podświetlone.
        """

        grid = [['-', '-', '#'], ['#', '-', '-']]
        bulbs = [[1, 0, None], [None, 0, 1]]
        self.assertTrue(check_constraint_all_white_cells_lit(grid, bulbs))

    def test_invalid(self):
        """
            ❌ Test negatywny: Przynajmniej jedno pole jest nieoświetlone.
        """

        grid = [['-', '-', '#'], ['#', '-', '-']]
        bulbs = [[0, 0, None], [None, 0, 1]]  # pole (0,0) nieoświetlone
        self.assertFalse(check_constraint_all_white_cells_lit(grid, bulbs))
