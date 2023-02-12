#!/usr/bin/python3
"""defines a function that returns a list of lists with N sized pascal's """


def pascal_triangle(n):
    """Returns a pascal's tringle os size n """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n)
    row = [1] * (i + 1)
    if i > 1:
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
