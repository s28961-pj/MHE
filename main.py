import argparse
import time

from input.algorithm_list import algorithms
from utils.print_matrix import print_matrix
from utils.read_from_file import read_from_file
from utils.read_from_standard_input import read_from_stdin


def main():

    # Stwórz parser argumentów
    parser = argparse.ArgumentParser(
        description="Uruchamianie algorytmów z linii komend."
    )
    parser.add_argument(
        "algorithm",
        choices=algorithms.keys(),
        help="Nazwa algorytmu, który chcesz uruchomić.",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=25,
        help="Liczba iteracji dla algorytmu (opcjonalne). Domyślnie: 25.",
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Ścieżka do pliku z planszą wejściową.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Tryb szczegółowy (opcjonalne).",
    )


    # Parsuj argumenty
    args = parser.parse_args()

    # Wyświetl informacje o wywołaniu dla użytkownika
    if args.verbose:
        print(f"Wybrano algorytm: {args.algorithm}")
        print(f"Liczba iteracji: {args.iterations}")

    # Wczytaj planszę
    if args.input:
        board = read_from_file(args.input)  # Wczytywanie z pliku
    else:
        board = read_from_stdin()  # Wczytywanie z wejścia standardowego

    # Wywołaj odpowiedni algorytm
    algorithm_function = algorithms[args.algorithm]
    algorithm_function()


if __name__ == '__main__':
    main()

