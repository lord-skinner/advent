import sys
import re
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math

# Read input data and parse it into bricks
D = open('input.txt').read().strip()
L = D.split('\n')

# Parse bricks and store them in a list (BS)
BS = []
for line in L:
    st, ed = line.split('~')
    sx, sy, sz = map(int, st.split(','))
    ex, ey, ez = map(int, ed.split(','))
    B = []
    if sx == ex and sy == ey:
        assert sz <= ez
        B.extend((sx, sy, z) for z in range(sz, ez + 1))
    elif sx == ex and sz == ez:
        assert sy <= ey
        B.extend((sx, y, sz) for y in range(sy, ey + 1))
    elif sy == ey and sz == ez:
        assert sx <= ex
        B.extend((x, sy, sz) for x in range(sx, ex + 1))
    else:
        assert False  # This should not happen
    BS.append(B)

# Initialize the seen set to track all occupied positions
SEEN = set((x, y, z) for B in BS for (x, y, z) in B)

# Falling brick simulation loop
while True:
    any_moved = False
    for i, B in enumerate(BS):
        ok = True
        for (x, y, z) in B:
            if z == 1:
                ok = False
            if (x, y, z - 1) in SEEN and (x, y, z - 1) not in B:
                ok = False
        if ok:
            any_moved = True
            for (x, y, z) in B:
                SEEN.remove((x, y, z))
                SEEN.add((x, y, z - 1))
            BS[i] = [(x, y, z - 1) for (x, y, z) in B]
    if not any_moved:
        break

# Count bricks that do not fall
p1 = 0
p2 = 0
for i, B in enumerate(BS):
    FALL = set()
    SEEN_COPY = SEEN.copy()  # Only copy SEEN when absolutely needed

    # Remove the current brick's positions from SEEN
    for (x, y, z) in B:
        SEEN_COPY.remove((x, y, z))

    # Try to make all other bricks fall
    while True:
        any_fallen = False
        for j, C in enumerate(BS):
            if j == i:  # Skip the current brick
                continue
            ok = True
            for (x, y, z) in C:
                if z == 1:
                    ok = False
                if (x, y, z - 1) in SEEN_COPY and (x, y, z - 1) not in C:
                    ok = False
            if ok:
                FALL.add(j)
                for (x, y, z) in C:
                    SEEN_COPY.remove((x, y, z))
                    SEEN_COPY.add((x, y, z - 1))
                BS[j] = [(x, y, z - 1) for (x, y, z) in C]
                any_fallen = True
        if not any_fallen:
            break

    # Count static and falling bricks
    if len(FALL) == 0:
        p1 += 1
    p2 += len(FALL)

# Output results
print(p1)
print(p2)
