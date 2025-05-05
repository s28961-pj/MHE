import unittest
from functions.optimization.objective_function import objective_function


class TestObjectiveUnlitCells(unittest.TestCase):
    def test_unlit_cells(self):
        """
            Testuje sytuację, gdy puste pola nie są oświetlone.
            W tej siatce brak żarówek, więc wszystkie puste pola (-) są nieoświetlone.
            Oczekujemy kary za każde nieoświetlone pole.
        """

        grid = [
            ['-', '-', '-'],
            ['-', '#', '-']
        ]
        bulbs = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertGreater(objective_function(grid, bulbs), 0)
