def read_from_file(file_path):

    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    print("Wczytano grid:")
    for line in grid:
        print("".join(line))

    return grid