def solve_n_queens(n):
    def dfs(queens, xy_dif, xy_sum):
        p = len(queens)
        # end condition
        if p == n:
            solutions.append(queens)
            return
        for q in range(n):
            # continue condition
            # when a location (x, y) is occupied, other locations (p, q) where
            # p + q == x + y or p - q == x - y would be invalid
            if q not in queens and (p - q not in xy_dif) and (p + q not in xy_sum):
                dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
    solutions = []
    dfs([], [], [])
    # convert the result to required format
    result = []
    for solution in solutions:
        board = []
        for i in solution:
            row = "." * i + "Q" + "." * (n - i - 1)
            board.append(row)
        result.append(board)
    return result
