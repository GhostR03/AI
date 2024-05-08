def isSafe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solveNQueen(board, row, N, count):
    if row == N:
        # All queens have been placed, solution found
        count[0] += 1
        print("Solution", count[0], ":")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=" ")
            print()
        print()
        return

    for col in range(N):
        if isSafe(board, row, col, N):
            # Place queen at board[row][col]
            board[row][col] = 1

            # Recursively solve for next row
            solveNQueen(board, row + 1, N, count)

            # Backtrack and remove the queen
            board[row][col] = 0


def main():
    N = int(input("Enter the number of queens: "))
    board = [[0] * N for i in range(N)]
    count = [0]

    solveNQueen(board, 0, N, count)

    print("Total solutions:", count[0])


main()




























#
# This code solves the N-Queens problem using a backtracking approach. Here's a brief explanation of how it works:
#
# 1. **isSafe(board, row, col, N):**
#    - This function checks if it's safe to place a queen at position (row, col) on the board. It checks if there are no queens in the same column, upper left diagonal, and upper right diagonal.
#
# 2. **solveNQueen(board, row, N, count):**
#    - This function is the core of the N-Queens problem solver. It uses recursion to try different configurations of queen placements.
#    - If all queens are placed successfully (row == N), it prints the solution and increments the count of solutions found.
#    - For each row, it tries placing the queen in each column where it's safe to do so and recursively solves for the next row.
#    - If placing a queen leads to an invalid configuration, it backtracks and removes the queen from that position.
#
# 3. **main():**
#    - This function takes the input N, the number of queens, from the user.
#    - It initializes an empty board of size N x N and a count variable to keep track of the number of solutions.
#    - It calls solveNQueen to start solving the N-Queens problem.
#    - After solving, it prints the total number of solutions found.
#
#
#
#
# **Sample Input:**
# ```
# Enter the number of queens: 4
# ```
#
# **Expected Output:**
# ```
# Solution 1 :
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0
#
# Solution 2 :
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0
#
# Total solutions: 2
# ```
#
# In this example, the user inputs the number of queens as 4 (`N = 4`). The program then finds and prints two possible solutions for placing 4 queens on a 4x4 chessboard without attacking each other. Each solution is represented by a matrix where '1' indicates the position of a queen and '0' indicates an empty cell. The program also prints the total number of solutions found, which is 2 in this case.
#
