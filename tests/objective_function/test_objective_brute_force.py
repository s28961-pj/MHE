import itertools
from functions.optimization.objective_function import objective_function


def brute_force_best_solution(grid, max_attempts=100000, max_seconds=10):
    """
        Przeszukuje wszystkie możliwe rozmieszczenia żarówek na białych polach,
        z ograniczeniem na liczbę prób i czas działania.

        :param grid: Plansza gry
        :param max_attempts: maksymalna liczba kombinacji do sprawdzenia
        :param max_seconds: maksymalny czas działania (sekundy)
        :return: najlepsza macierz bulbs, najlepszy wynik
    """

    rows, cols = len(grid), len(grid[0])
    white_cells = [(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == '-']
    num_white = len(white_cells)

    best_bulbs = None
    best_score = float('inf')

    # Wszystkie kombinacje: każda komórka biała ma żarówkę (1) lub nie (0)
    for combination in itertools.product([0, 1], repeat=num_white):
        # Zbuduj macierz bulbs
        bulbs = [[0 for _ in range(cols)] for _ in range(rows)]
        for (row, col), val in zip(white_cells, combination):
            bulbs[row][col] = val

        score = objective_function(grid, bulbs)
        if score < best_score:
            best_score = score
            best_bulbs = bulbs

    return best_bulbs, best_score
