from algorithms.brute_force.brute_force import brute_force
from algorithms.genetic_algorithm.genetic_algorithm import genetic_algorithm
from algorithms.hill_climbing.hill_climbing import hill_climbing
from algorithms.hill_climbing_random.hill_climbing_random import hill_climbing_random
from algorithms.tabu_search.tabu_search import tabu_search

algorithms = {
        "Brute_Force": brute_force,
        "Random_Solution": random_solution,
        "Tabu_Search": tabu_search,
        "Hill_Climbing": hill_climbing,
        "Hill_Climbing_Random": hill_climbing_random,
        "Simulated_Annealing": simulated_annealing,
        "Genetic_Algorithm": genetic_algorithm
}