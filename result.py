from data.data import sample_grid
from functions.constraints.check_all_constraints import check_all_constraints
from functions.generate_akari_grid import generate_akari_grid
from functions.generate_decision_variables import generate_decision_variables
from functions.print_grid import print_grid
from tests.objective_function.test_objective_brute_force import brute_force_best_solution


grid = [
    ['-', '-', '#'],
    ['-', '2', '-'],
    ['#', '-', '-']
]

best_bulbs, best_score = brute_force_best_solution(sample_grid, max_attempts=1000, max_seconds=5)

print("Najlepszy wynik:", best_score)
for row in best_bulbs:
    print(row)
