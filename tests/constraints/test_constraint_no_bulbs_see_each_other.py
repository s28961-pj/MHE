import unittest
from functions.constraints.check_constraint_no_bulbs_see_each_other import check_constraint_no_bulbs_see_each_other


class TestConstraintNoBulbsSeeEachOther(unittest.TestCase):
    def test_valid(self):
        """
            ✅ Test pozytywny: Żarówki są umieszczone w sposób, który nie powoduje świecenia na siebie.
        """

        grid = [['-', '-', '#', '-', '-']]
        bulbs = [[1, 0, None, 1, 0]]
        self.assertTrue(check_constraint_no_bulbs_see_each_other(grid, bulbs))

    def test_invalid(self):
        """
            ❌ Test negatywny: Żarówki umieszczone w jednej linii bez przeszkody (#) świecą na siebie.
        """

        grid = [['-', '-', '-', '-', '-']]
        bulbs = [[1, 0, 0, 0, 1]]  # żarówki się widzą w tym samym wierszu
        self.assertFalse(check_constraint_no_bulbs_see_each_other(grid, bulbs))
