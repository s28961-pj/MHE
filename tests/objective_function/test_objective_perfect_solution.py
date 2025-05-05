import unittest
from functions.optimization.objective_function import objective_function


class TestObjectivePerfectSolution(unittest.TestCase):
    def test_perfect_solution(self):
        """
            Testuje idealne rozwiązanie siatki.
            Wszystkie puste pola są oświetlone, żadna żarówka nie świeci na inną,
            wszystkie warunki liczbowe na ścianach są spełnione.
            Oczekujemy wartości celu = 0 (brak kar).
        """

        grid = [
            ['-', '-', '#', '1'],
            ['#', '-', '-', '-'],
            ['-', '-', '#', '-'],
            ['1', '-', '-', '-']
        ]
        bulbs = [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0]
        ]
        self.assertEqual(objective_function(grid, bulbs), 0)
