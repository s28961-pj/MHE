def generate_decision_variables(grid):
    """
    Generuje zmienne decyzyjne na podstawie planszy Akari.
    Dla białych pól: 0 (brak żarówki na starcie)
    Dla ścian i pól z liczbami: None (nie można umieścić żarówki)
        :param grid: Lista list zawierająca znaki '-', '#', '0'-'4'
        :return: lista list z wartościami 0 lub None
    """

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Pusta tablica w podanym rozmiarze
    decision_variables = [[None for _ in range(cols)] for _ in range(rows)]

    # Generowanie listy zmiennych decyzyjnych
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '-':
                decision_variables[row][col] = 0
            else:
                decision_variables[row][col] = None

    return decision_variables
