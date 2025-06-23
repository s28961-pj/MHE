def read_from_stdin():

    print("Wprowadź dane planszy (grid). Wprowadź pustą linię aby zakończyć:")

    lines = []

    while True:
        line = input()
        if not line.strip():  # Pusta linia kończy wprowadzanie
            break
        # Konwersja każdego wiersza na listę znaków
        lines.append(list(line.strip()))

    print("Wprowadzono grid:")
    for line in lines:
        print("".join(line))

    return lines