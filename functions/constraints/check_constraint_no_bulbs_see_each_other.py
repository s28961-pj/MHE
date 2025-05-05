from functions.utils.is_valid_position import is_valid_position


def check_constraint_no_bulbs_see_each_other(grid, bulbs):
    """
        Sprawdza, czy żarówki się nawzajem widzą.
        Dwie żarówki „widzą się”, jeśli znajdują się w tej samej linii (rzędzie lub kolumnie)
        i między nimi nie ma ściany (zwykłej lub numerowanej).

        :param grid: Siatka gry zawierająca:
                '-' - puste pole,
                '#' - ściana,
                '0'-'4' - ściana z liczbą żarówek, które mają przylegać.
        :param bulbs: Tabela żarówek:
                1 - oznacza obecność żarówki,
                None - brak żarówki.
        :return bool: True, jeśli żadna żarówka nie oświetla innej żarówki w swoim rzędzie/kolumnie, False w przeciwnym razie.

        delta_row, delta_col - zmiana wiersza/kolumny
        neighbour_row, neighbour_col - sąsiedni wiersz/kolumna
    """

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if bulbs[row][col] == 1:
                for delta_row, delta_col in [(-1,0), (1,0), (0,-1), (0,1)]:
                    neighbour_row, neighbour_col = row + delta_row, col + delta_col
                    while is_valid_position(grid, neighbour_row, neighbour_col):
                        if grid[neighbour_row][neighbour_col] != '-':
                            break
                        if bulbs[neighbour_row][neighbour_col] == 1:
                            return False
                        neighbour_row += delta_row
                        neighbour_col += delta_col
    return True