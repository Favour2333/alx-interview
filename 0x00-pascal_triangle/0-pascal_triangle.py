#!/usr/bin/python3
"""
A pascal's triangle module.
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers which represents
    the Pascal's triangle of a given integer.

    Args:
    n (int): Number of rows of the triangle

    Returns:
    List of lists of integers representing the Pascal’s triangle
    """

    triangle = []

    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
