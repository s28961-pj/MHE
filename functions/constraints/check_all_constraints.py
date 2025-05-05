from functions.constraints.check_constraint_all_white_cells_lit import check_constraint_all_white_cells_lit
from functions.constraints.check_constraint_no_bulbs_on_walls import check_constraint_no_bulbs_on_walls
from functions.constraints.check_constraint_no_bulbs_see_each_other import check_constraint_no_bulbs_see_each_other
from functions.constraints.check_constraint_wall_numbers_correct import check_constraint_wall_numbers_correct


def check_all_constraints(grid, bulbs):
    """
        Sprawdza, czy wszystkie ograniczenia gry Akari są spełnione dla danej siatki i rozmieszczenia żarówek.
        :param grid: Siatka zawierająca znaki '-', '#', '0'-'4'.
        :param bulbs: Rozmieszczenie żarówek, gdzie 1 oznacza żarówkę, a None brak żarówki.
        :return bool: True, jeśli wszystkie ograniczenia są spełnione, False w przeciwnym razie.
    """

    return (
        check_constraint_no_bulbs_on_walls(grid, bulbs) and
        check_constraint_no_bulbs_see_each_other(grid, bulbs) and
        check_constraint_wall_numbers_correct(grid, bulbs) and
        check_constraint_all_white_cells_lit(grid, bulbs)
    )