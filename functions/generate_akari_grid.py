import random

def generate_akari_grid(size, wall_prob=0.15, number_prob=0.1):

    # Walidacja rozmiaru planszy <3,10>
    if not (3 <= size <= 20):
        print("Rozmiar musi być w zakresie od 3 do 10.")
        return


    # Pusta plansza kwadratowa w podanym rozmiarze
    grid = [['-' for _ in range(size)] for _ in range(size)]


    # Generowanie zawartości planszy
    for row in range(size):
        for col in range(size):

            # Nie umieszczaj ścian w rogach i na brzegach, żeby nie było bezsensownych ograniczeń
            if (0 < row < size - 1) and (0 < col < size - 1):
                roll = random.random()
                if roll < number_prob:

                    # Umieść czarną ścianę z numerem (0–4) tylko jeśli ma wystarczająco dużo sąsiadów
                    neighbors = 0
                    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == '-':
                            neighbors += 1
                    if neighbors > 0:
                        grid[row][col] = str(random.randint(0, min(4, neighbors)))
                elif roll < wall_prob + number_prob:

                    # Umieść zwykłą ścianę
                    grid[row][col] = '#'

    return grid
