from ortools.linear_solver import pywraplp
from math import ceil

#Not working, it always says there is no solution, but nevermind
def find_seats(rows, seats_per_row, groups):
    solver = pywraplp.Solver.CreateSolver('SCIP')

    row_range = range(1, rows + 1)
    seat_range = range(1, seats_per_row + 1)
    group_range = range(1, len(groups) + 1)

    middle_row = ceil(rows / 2)
    middle_seat = ceil(seats_per_row / 2)

    pairs = [(i, k) for i in group_range for k in seat_range]

    # coefficients for the objective function
    c = {}
    for i in row_range:
        for j in seat_range:
            c[i, j] = 1 + abs(i + 1 - middle_row) + abs(j + 1 - middle_seat)

    # z[i, j, k] = 1 if group i is placed in row j starting at column k
    z = {}
    for i in group_range:
        for j in row_range:
            for k in seat_range:
                z[i, j, k] = solver.BoolVar(f'z_{i}_{j}_{k}')

    # every group must be allocated
    for i in group_range:
        solver.Add(sum(z[i, j, k] for j in row_range for k in seat_range) == 1)

    # conflict constrain
    for j in row_range:
        solver.Add(sum(z[i1, j, k1] + z[i2, j, k2] for (i1, k1) in pairs for (i2, k2) in pairs if
                       (k1 <= k2 <= k1 + groups[i1-1])) <= 1)

    # solver.Minimize(solver.Sum([y[j] for j in data['bins']]))
    objective = solver.Objective()
    for i in group_range:
        for j in row_range:
            for k in seat_range:
                objective.SetCoefficient(z[i, j, k], sum(c[j, b] for b in range(k + 1, k + groups[i - 1]) if k + groups[i - 1]-1<=seats_per_row ))
    objective.SetMinimization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'Total score: {objective.Value()}')
        total_weight = 0
        for i in group_range:
            for j in row_range:
                for k in seat_range:
                    if z[i, j, k].solution_value() > 0:
                        print(
                            f"Group {i} is allocated in row {j} from seat {k} to {k + groups[i - 1]}."
                        )
    else:
        print('The problem does not have an optimal solution.')

    print('Number of variables =', solver.NumVariables())
