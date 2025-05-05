def print_grid(grid, with_numbers=False):
    """
    Drukuje siatkę Akari z ramką i opcjonalną numeracją.
        :param grid: Lista list z wartościami ('-', '#', '0'-'4', 'B', '*' itp.),
        :param with_numbers: jeśli True, dodaje numerację wierszy i kolumn
    """

    print(f"\n 🧩 Plansza Akari:\n")

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if with_numbers:
        print('  +' + '---' * cols + '+')
    else:
        print('+' + '---' * cols + '+')

    for i, row in enumerate(grid):
        if with_numbers:
            print(f'{i + 1:2}|', end='')
        else:
            print('|', end='')
        for cell in row:
            print(f' {cell} ', end='')
        print('|')

    if with_numbers:
        print('  +' + '---' * cols + '+')
        print('   ' + ''.join(f'{j + 1:^3}' for j in range(cols)))
    else:
        print('+' + '---' * cols + '+')
