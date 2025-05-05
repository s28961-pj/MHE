import unittest
from functions.constraints.check_constraint_no_bulbs_on_walls import check_constraint_no_bulbs_on_walls


class TestConstraintNoBulbsOnWalls(unittest.TestCase):
    def test_valid(self):
        """
            ✅ Test pozytywny: Żarówki znajdują się tylko na pustych polach ('-').
        """

        grid = [['-', '#'], ['#', '-']]
        bulbs = [[1, None], [None, 1]]
        self.assertTrue(check_constraint_no_bulbs_on_walls(grid, bulbs))

    def test_invalid(self):
        """
            ❌ Test negatywny: Któraś z żarówek znajduje się na ścianach (zwykłych i numerowanych).
        """

        grid = [['-', '#'], ['#', '2']]
        bulbs = [[1, 1], [None, 1]]  # żarówki na ścianach
        self.assertFalse(check_constraint_no_bulbs_on_walls(grid, bulbs))
