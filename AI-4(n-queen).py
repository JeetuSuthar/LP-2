def is_safe(queens, row, col):
    for c in range(col):
        if queens[c] == row or abs(queens[c] - row) == abs(c - col):
            return False
    return True

def solve_n_queens_util(queens, col, n):
    if col == n:
        return queens[:]
    for row in range(n):
        if is_safe(queens, row, col):
            queens[col] = row
            result = solve_n_queens_util(queens, col + 1, n)
            if result:
                return result
    return None

def print_solution(queens):
    n = len(queens)
    for r in range(n):
        row = ["Q" if queens[c] == r else "." for c in range(n)]
        print(" ".join(row))
    print()

if __name__ == "__main__":
    n = int(input("Enter value of N: "))
    queens = [-1] * n
    result = solve_n_queens_util(queens, 0, n)
    if result:
        print(f"Found a solution for {n}-Queens problem:")
        print_solution(result)
    else:
        print("Solution does not exist")