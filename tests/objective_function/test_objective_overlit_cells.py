import unittest
from functions.optimization.objective_function import objective_function


class TestObjectiveOverlitCells(unittest.TestCase):
    def test_overlit_cells(self):
        """
            Testuje konflikt świetlny: dwie żarówki świecą na siebie.
            Żarówki w tej samej linii bez przeszkody (#) powodują błąd.
            Oczekujemy, że funkcja celu wykryje konflikt i zwróci karę.
        """

        grid = [['-', '-', '-']]
        bulbs = [[1, 0, 1]]  # obie żarówki świecą na siebie
        self.assertGreater(objective_function(grid, bulbs), 0)
