def is_valid_position(grid, row, col):
    return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))