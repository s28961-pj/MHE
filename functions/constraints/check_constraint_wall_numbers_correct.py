from functions.utils.count_adjacent_bulbs import count_adjacent_bulbs
from functions.utils.is_valid_position import is_valid_position


def check_constraint_wall_numbers_correct(grid, bulbs):
    """
        Sprawdza, czy liczba żarówek wokół takich ścian jest zgodna z wartością cyfry.

        :param grid: Plansza gry zawierająca:
                '-' - puste pole,
                '#' - ściana bez cyfry,
                '0'-'4' - ściana z wymaganą liczbą przylegających żarówek.
        :param bulbs: Siatka o tej samej wielkości co grid:
                1 - obecność żarówki,
                None - brak żarówki.
        :return bool: True, jeśli każda ściana z cyfrą ma dokładnie tylu sąsiadujących żarówek, ile wskazuje cyfra.
                  False w przeciwnym razie.
        """

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in '01234':
                expected = int(grid[row][col])
                if count_adjacent_bulbs(grid, bulbs, row, col) != expected:
                    return False
    return True