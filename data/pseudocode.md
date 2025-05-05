
Algorithm 1 Solving puzzles without numbers.
Require: puzzle without numbers
Ensure: solution
    1: while dark cells left do
    2: place light on (random) dark cell
    3: end while
    4: return placed lights

Algorithm 2 Solving puzzles with only 4’s.
Require: puzzle with only 4’s
Ensure: solution
    1: for every 4-cell do
    2: place light on all neighbours
    3: end for
    4: while dark cells left do
    5: place light on random dark cell
    6: end while
    7: return placed lights

Algorithm 3 Checking solvability of puzzles with only 4’s.
    1: if 4-cell has less than 4 placable neighbours then
    2: return null
    3: end if

Algorithm 4 Trivial Solver
Require: puzzle
Ensure: placement of trivial light bulbs
    1: for every 0-cell do
    2: mark every neighbour as implacable
    3: end for
    4: while n-cell with exactly n placable neighbours do
    5: place light on every neighbour
    6: mark newly lit cells as implacable
    7: end while
    8: return placed lights(, implacable cells)

Algorithm 5 Backtrack Function
    1: function backtrack(puzzle, candidates, solution, solutions)
    2: if puzzle is solved then
    3: append solution to solutions
    4: return
    5: end if
    6: if no candidates or a wall is unsatisfiable then
    7: return
    8: end if
    9: place a light bulb on the next candidate
    10: append candidate to solution
    11: backtrack(puzzle, candidates, solution, solutions)
    12: remove light bulb from the candidate
    13: remove candidate from solution
    14: backtrack(puzzle, candidates, solution, solutions)
    15: end function

Algorithm 6 Backtrack Solver
Require: puzzle
Ensure: solutions
    1: find base solution using the trivial solver
    2: sort the light bulb candidates
    3: backtrack(puzzle, candidates, solution, solutions)
    4: return solutions

Algorithm 7 Puzzle Generator
Require: w (width) ≥ 1, h (height) ≥ 1, s (start) ≥ 0, n (step) ≥ 1
Ensure: puzzle solution is unique
    1: create an empty puzzle of size w × h
    2: place s new wall(s)
    3: solve puzzle and place numbers on all walls
    4: while puzzle solution is not unique do
    5: remove all numbers
    6: place n new wall(s)
    7: solve puzzle and place numbers on all walls
    8: end while
    9: remove number constraints invariant under solution uniqueness
    10: return puzzle


Algorithm 8 Remove some number constraints.
    1: for wall with a number constraint do
    2: remove number constraint
    3: if puzzle solution is not unique then
    4: restore number constraint
    5: end if
    6: end for
