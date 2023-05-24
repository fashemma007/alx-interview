#!/usr/bin/python3
"""module docs for 0-nqueens.py"""
import sys


def check_args() -> int:
    """handles parsing of arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    num_queens = sys.argv[1]
    try:
        num_queens = int(num_queens)
    except ValueError:
        print("N must be a number")
        exit(1)
    if num_queens < 4:
        print("N must be at least 4")
        exit(1)
    return num_queens


def nqueens(n: int):
    """
    The nqueens function

    :param n: int: Specify the size of the board
    :return: A list of lists
    """
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    columns = set()
    positive_diags = set()  # row + cols
    negative_diags = set()  # row - cols
    results = []

    board = [["_"] * n for _ in range(n)]

    def backtrackker(row):
        """
        The backtrackker function is a recursive function that takes in the
        `row` number as an argument. The base case of the recursion is when we
        have reached the last `row`, and then we append our solution to results
        If not, for each column in this row, if it's already occupied by
        another queen or if it's on a diagonal with another queen (which can be
        checked using positive_diags and negative_diags), then continue to next
        column. Otherwise add this position to columns, positive_diags and
        negative_diags so that other queens cannot occupy these positions later
        on. Then place a &quot;Q&quot; on the board

        :param row: Keep track of the current row we are on
        :return: All the possible solutions
        """
        if row == n:
            # board_copy = board[row]
            board_copy = [" ".join(r) for r in board]
            results.append(board_copy)
            return
        for cols in range(n):
            if cols in columns\
                or (row + cols) in positive_diags\
                    or (row - cols) in negative_diags:
                continue
            columns.add(cols)
            positive_diags.add(row + cols)
            negative_diags.add(row - cols)
            board[row][cols] = "Q"
            backtrackker(row + 1)
            # clean the board to get other solutions
            columns.remove(cols)
            positive_diags.remove(row + cols)
            negative_diags.remove(row - cols)
            board[row][cols] = "_"
    backtrackker(0)

    for res in results:
        rez = []
        # print(r)
        for queen in res:
            rez.append(queen.split())
        # print(rez)
        valz = []
        for i, a in enumerate(rez):
            key = [i, a.index('Q')]
            valz.append(key)
        print(valz)
    # return results


if __name__ == "__main__":
    queens = check_args()
    nqueens(queens)
