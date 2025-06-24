import random
import copy

from utils.print_matrix import print_matrix


def random_solution(board, bulb_probability=0.3):

    print("Uruchamianie algorytmu Generate Random Solution...")
    solution = copy.deepcopy(board)

    for y in range(len(solution)):
        for x in range(len(solution[0])):
            if solution[y][x] == "-":
                if random.random() < bulb_probability:
                    solution[y][x] = "B"

    print_matrix(solution)

    print("Zakończenie pracy algorytmu Generate Random Solution...")

    return solution
