#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
import sys
import itertools
import math

class Dir(Enum):
    left = 1
    right = 2
    up = 3
    down = 4

RL = [Dir.right]
DL = [Dir.down]
LL = [Dir.left, Dir.left]
UL = [Dir.up, Dir.up]
RL2 = [Dir.right, Dir.right]

res = [list(RL) + list(DL) + list(LL) + list(UL) + list(RL2)]

N = int(sys.argv[1])
squares = [i**2 for i in range(N+1)]
odd_squares = list(filter(lambda x: x % 2 == 1, squares))
print(odd_squares)

for i in odd_squares[2:]:
    res.append(RL)

    DL = DL + [Dir.down, Dir.down]
    res.append(list(DL))

    LL = LL + [Dir.left, Dir.left]
    res.append(list(LL))

    UL = UL + [Dir.up, Dir.up]
    res.append(list(UL))

    RL2 = RL2 + [Dir.right, Dir.right]
    res.append(list(RL2))

# size of list should be N^2-1
res = list(itertools.chain(*res))
res = res[:(N**2 - 1)]
#print(len(res))

matrix = [[0 for x in range(N)] for x in range(N)]

coord = [math.floor((N-1) / 2), math.floor((N-1) / 2)]
counter = 0
matrix[coord[0]][coord[1]] = counter
counter = 1
print(coord)
for d in res:
    if d == Dir.right:
        coord[1] += 1
    elif d == Dir.left:
        coord[1] -= 1
    elif d == Dir.up:
        coord[0] -= 1
    else:
        coord[0] += 1

    print(coord)
    matrix[coord[0]][coord[1]] = counter
    counter += 1

for i in range(N):
    print(matrix[i])

