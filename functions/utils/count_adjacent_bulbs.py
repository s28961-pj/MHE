from functions.utils.is_valid_position import is_valid_position


def count_adjacent_bulbs(grid, bulbs, row, col):
    """
        Zlicza liczbę żarówek (1) sąsiadujących z daną komórką (góra, dół, lewo, prawo).

        :param grid: Plansza z grą.
        :param bulbs: Siatka żarówek.
        :param row: Wiersz komórki.
        :param col: Kolumna komórki.
        :return: Liczba sąsiadujących żarówek.
    """

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if is_valid_position(grid, nr, nc) and bulbs[nr][nc] == 1:
            count += 1
    return count