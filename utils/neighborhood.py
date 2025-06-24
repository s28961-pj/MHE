import copy
import random

from algorithms.random_solution.random_solution import random_solution
from input.example import board
from utils.print_matrix import print_matrix


def change_neighborhood(solution):

    print("Uruchamianie modyfikacji Najbliższego Sąsiedztwa...")

    neighbor = copy.deepcopy(solution)

    height = len(neighbor)
    width = len(neighbor[0])

    # Tworzymy listę białych pól '-' i żarówek 'B' do edycji
    changing_solution = [(y, x) for y in range(height) for x in range(width) if neighbor[y][x] in {'-', 'B'}]

    # Jeśli nie ma pól do zmiany, zwracamy bieżące rozwiązanie
    if not changing_solution:
        return neighbor

    # Wybieramy losowe pole do zmiany
    y, x = random.choice(changing_solution)

    # Zamieniamy 'B' na '-' lub '-' na 'B'
    neighbor[y][x] = 'B' if neighbor[y][x] == '-' else '-'

    print_matrix(neighbor)

    print("Zakończenie modyfikacji Najbliższego Sąsiedztwa...")

    return neighbor

get_neighborhood(random_solution(board))