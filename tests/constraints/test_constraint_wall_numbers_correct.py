import unittest
from functions.constraints.check_constraint_wall_numbers_correct import check_constraint_wall_numbers_correct


class TestWallNumbersCorrect(unittest.TestCase):
    def test_valid(self):
        """
            ✅ Test pozytywny: Sprawdza, czy każda ściana z liczbą ma dokładnie tyle sąsiadujących żarówek.
        """

        grid = [['-', '1'], ['1', '-']]
        bulbs = [[1, None], [None, 1]]
        self.assertTrue(check_constraint_wall_numbers_correct(grid, bulbs))

    def test_invalid(self):
        """
            ❌ Test negatywny: Sprawdza, czy przynajmniej jedna ściana z liczbą ma zbyt mało sąsiadujących żarówek.
        """

        grid = [['-', '2'], ['1', '-']]
        bulbs = [[1, None], [None, 1]]  # przy ścianie 2 tylko 1 żarówka
        self.assertFalse(check_constraint_wall_numbers_correct(grid, bulbs))
