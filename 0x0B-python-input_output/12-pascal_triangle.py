#!/usr/bin/python3
"""pascal_traigle module."""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        prev_row = triangle[-1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i-1] + prev_row[i])
        row.append(1)
        triangle.append(row)

    return triangle
