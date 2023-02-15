#!/usr/bin/python3
"""A standalone module solving the nqueens problem"""
import sys


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    size = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
    sys.exit(1)

if size <= 4:
    print("N must be at least 4")
    sys.exit(1)

queens = [0] * size


def printsolution(queens):
    print("[[0, ", queens[0], "]", sep="", end="")
    for y, x in enumerate(queens[1:], 1):
        print(", [", y, ", ", x, "]", sep="", end="")
    print("]")


def queencalc(queen):
    """Recursive call queen position validator"""
    if queen == size:
        printsolution(queens)
        return
    for x in range(size):
        """horizontal board positions per queen"""
        nextx = 0
        for y in range(queen):
            qx = queens[y]
            if x == qx or x + queen == qx + y or x - queen == qx - y:
                nextx = 1
                break
            if nextx == 1:
                nextx = 0
                continue
            queens[queen] = x
            queencalc(queen + 1)


queencalc(0)
