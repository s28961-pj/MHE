from functions.constraints.check_constraint_all_white_cells_lit import check_constraint_all_white_cells_lit
from functions.constraints.check_constraint_no_bulbs_on_walls import check_constraint_no_bulbs_on_walls
from functions.constraints.check_constraint_no_bulbs_see_each_other import check_constraint_no_bulbs_see_each_other
from functions.constraints.check_constraint_wall_numbers_correct import check_constraint_wall_numbers_correct


def objective_function(grid, bulbs):
    """
        Liczy łączną liczbę naruszeń zasad.
        Im mniejszy wynik, tym lepsze rozmieszczenie żarówek.

        :param grid: Plansza gry (lista list)
        :param bulbs: rozmieszczenie żarówek (0/1 w tych samych wymiarach co grid)
        :return: int — suma naruszeń
    """

    violations = 0

    violations += check_constraint_all_white_cells_lit(grid, bulbs)
    violations += check_constraint_no_bulbs_on_walls(grid, bulbs)
    violations += check_constraint_no_bulbs_see_each_other(grid, bulbs)
    violations += check_constraint_wall_numbers_correct(grid, bulbs)

    return violations
