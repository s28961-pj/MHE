from input.example import board
from algorithms.random_search.random_solution import generate_random_solution
from utils.print_matrix import print_matrix


def goal_function(solution):

    print("Uruchamianie Algorytmu Celu...")
    print("--------------------------------")
    print_matrix(board)
    print("--------------------------------")
    print_matrix(solution)
    print("--------------------------------")

    height = len(solution)
    width = len(solution[0])

    lit = [[False for _ in range(width)] for _ in range(height)]
    penalty = 0

    # 1. Oświetlanie pól przez żarówki
    for y in range(height):
        for x in range(width):
            if solution[y][x] == "B":
                # Żarówki nie mogą się widzieć
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    while 0 <= nx < width and 0 <= ny < height:
                        if solution[ny][nx] in "#01234":
                            break
                        if solution[ny][nx] == "B":
                            penalty += 5  # żarówki się widzą
                        lit[ny][nx] = True
                        nx += dx
                        ny += dy
                lit[y][x] = True

    # 2. Sprawdzenie, czy wszystkie białe pola są oświetlone
    for y in range(height):
        for x in range(width):
            if solution[y][x] == "-" and not lit[y][x]:
                penalty += 3  # ciemne białe pole

    # 3. Sprawdzenie liczby żarówek wokół czarnych pól z liczbami
    for y in range(height):
        for x in range(width):
            if solution[y][x] in "01234":
                expected = int(solution[y][x])
                count = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        if solution[ny][nx] == "B":
                            count += 1
                penalty += abs(expected - count) * 2

    print(f"Wynik: {penalty}")

    return penalty  # im niższy wynik, tym lepiej

goal_function(generate_random_solution(board))
