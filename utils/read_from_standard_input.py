from utils.print_matrix import print_matrix


def read_from_stdin():

    print("Wprowadź dane planszy (grid). Wprowadź pustą linię aby zakończyć:")

    lines = []

    while True:
        line = input()
        if not line.strip():  # Pusta linia kończy wprowadzanie
            break
        lines.append(list(line.strip()))

    print("Wprowadzono grid:")
    print_matrix(lines)

    return lines