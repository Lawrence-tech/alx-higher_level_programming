#!/usr/bin/python3
"""defines a function that returns a list of lists with N sized pascal's """


def pascal_triangle(n):
    """Returns a pascal's tringle os size n """
    triangle = []
    if n <= 0:
        return []
    n -= 1
    for row in range(n + 1):
        triangle.append([])
        triangle[row].append(1)
        for col in range(int(row / 2)):
            triangle[row].append(triangle[row - 1][col] + triangle[row - 1]
                                 [col + 1])
            if row % 2 == 1:
                triangle[ro].extend(triangle[row][::-1])
            else:
                triangle[row].extend(triangle[row][-2::-1])
        return triangle
