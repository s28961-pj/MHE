import copy
import random

def generate_neighbors(grid, bulbs):
    """
        Zwraca listę bliskich sąsiadów danego rozwiązania.
        Każdy sąsiad to kopia bulbs z jedną żarówką dodaną, usuniętą lub przesuniętą.
    """

    neighbors = []
    rows, cols = len(grid), len(grid[0])

    # Szukamy wszystkich białych pól i aktualnych żarówek
    white_cells = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '-']
    bulb_positions = [(r, c) for r in range(rows) for c in range(cols) if bulbs[r][c] == 1]

    # Dodanie żarówki w losowym białym polu (jeśli nie ma tam jeszcze żarówki)
    for r, c in white_cells:
        if bulbs[r][c] == 0:
            new_bulbs = copy.deepcopy(bulbs)
            new_bulbs[r][c] = 1
            neighbors.append(new_bulbs)

    # Usunięcie istniejącej żarówki
    for r, c in bulb_positions:
        new_bulbs = copy.deepcopy(bulbs)
        new_bulbs[r][c] = 0
        neighbors.append(new_bulbs)

    # Przesunięcie żarówki: usuń jedną, dodaj inną (w białym polu bez żarówki)
    for (r1, c1) in bulb_positions:
        for (r2, c2) in white_cells:
            if bulbs[r2][c2] == 0:
                new_bulbs = copy.deepcopy(bulbs)
                new_bulbs[r1][c1] = 0
                new_bulbs[r2][c2] = 1
                neighbors.append(new_bulbs)

    return neighbors
