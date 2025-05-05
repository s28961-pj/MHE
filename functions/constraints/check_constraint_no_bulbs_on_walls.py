def check_constraint_no_bulbs_on_walls(grid, bulbs):
    """
        Sprawdza ograniczenie gry Akari, że żarówki mogą być umieszczane tylko na pustych polach ('-').

        :param grid: Siatka gry zawierająca pola:
            '-' - puste pole,
            '#' - ściana,
            '0'-'4' - ściana z liczbą żarówek, które muszą do niej przylegać.
        :param bulbs: Siatka tej samej wielkości, zawierająca:
            1 - jeśli na danym polu znajduje się żarówka,
            None - brak żarówki.
        :return: True, jeśli żadna żarówka nie została umieszczona na ścianie, False w przeciwnym razie.
    """

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if bulbs[row][col] == 1 and grid[row][col] != '-':
                return False
    return True