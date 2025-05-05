from functions.utils.is_valid_position import is_valid_position


def check_constraint_all_white_cells_lit(grid, bulbs):
    """
        Sprawdza, czy wszystkie białe pola ('-') na planszy są oświetlone.
        Oświetlenie działa poziomo i pionowo aż do przeszkody (np. czarnego pola).

        :param grid: 2D lista znaków, gdzie '-' oznacza białe pole
        :param bulbs: 2D lista zmiennych decyzyjnych, gdzie 1 oznacza żarówkę, 0 brak
        :return: True, jeśli każde białe pole jest oświetlone, False w przeciwnym razie

        delta_row, delta_col - zmiana wiersza/kolumny
        neighbour_row, neighbour_col - sąsiedni wiersz/kolumna
        lit — oświetlona
    """

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '-':
                lit = bulbs[row][col] == 1
                for delta_row, delta_col in [(-1,0), (1,0), (0,-1), (0,1)]:
                    neighbour_row, neighbour_col = row + delta_row, col + delta_col
                    while is_valid_position(grid, neighbour_row, neighbour_col):
                        if grid[neighbour_row][neighbour_col] != '-':
                            break
                        if bulbs[neighbour_row][neighbour_col] == 1:
                            lit = True
                            break
                        neighbour_row += delta_row
                        neighbour_col += delta_col
                    if lit:
                        break
                if not lit:
                    return False
    return True
