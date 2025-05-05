def is_lit(grid, row, col):
    """
        Sprawdza, czy pole (row, col) jest oświetlone przez jakąkolwiek żarówkę
    """

    if grid[row][col] != ' ':
        return True  # Nie jest puste, więc nie musi być oświetlone

    # Sprawdzamy 4 kierunki: góra, dół, lewo, prawo
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = row + dx, col + dy
        while 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] in ('#', '0', '1', '2', '3', '4'):
                break
            if grid[nx][ny] == 'B':
                return True
            nx += dx
            ny += dy
    return False