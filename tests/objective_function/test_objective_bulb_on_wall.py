import unittest
from functions.optimization.objective_function import objective_function


class TestObjectiveBulbOnWall(unittest.TestCase):
    def test_bulb_on_wall(self):
        """
            Testuje błąd: umieszczenie żarówki na ścianie (#).
            W grze Akari żarówki mogą być tylko na pustych polach (-).
            Oczekujemy, że funkcja celu zwróci wartość większą niż 0 (kara).
        """

        grid = [
            ['-', '#', '-', '-'],
            ['#', '-', '-', '-']
        ]
        bulbs = [
            [1, 1, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertGreater(objective_function(grid, bulbs), 0)
