from utils.print_matrix import print_matrix


def read_from_file(file_path):

    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    print("Wczytano grid:")
    print_matrix(grid)

    return grid
