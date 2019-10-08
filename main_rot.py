#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    matrix_r = matrix

    for z in range(0, min(m,n) // 2):
        queue = []
        queue_2 = []

        for j in range(z, n - z):
            queue.append(matrix[z][j])
            queue_2.append(matrix[m - z - 1][n - z - (j + 1)])
        for i in range(z + 1, m - z - 1):
            queue.append(matrix[i][n - 1 - z])
            queue_2.append(matrix[m - z - i][z])
        # for j2 in range(z, n - z)[::-1]:
        #    queue.append(matrix[m - z - 1][j2])
        # for i2 in range(z + 1, m - z - 1)[::-1]:
        #     queue.append(matrix[i2][z])
        queue.extend(queue_2)
        print(queue)
        for _ in range(0, r):
            queue.append(queue.pop(0))
        print(queue)

        for j in range(z, n - z):
            matrix_r[z][j] = queue.pop(0)
        for i in range(z + 1, m - z - 1):
            matrix_r[i][n - 1 - z] = queue.pop(0)
        for j2 in range(z, n - z)[::-1]:
            matrix_r[m - z - 1][j2] = queue.pop(0)
        for i2 in range(z + 1, m - z - 1)[::-1]:
            matrix_r[i2][z] = queue.pop(0)

    return matrix_r

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    mat = matrixRotation(matrix, r)
    print(mat)
    for row in mat:
        print (' '.join(map(str,row)))
