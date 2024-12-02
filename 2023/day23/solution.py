import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math

# Read input data from the file and prepare the grid
D = open('input.txt').read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]
R = len(G)  # Number of rows
C = len(G[0])  # Number of columns

# Set recursion limit for deep recursion cases
sys.setrecursionlimit(10**6)

def solve(part1):
    V = set()  # Set to store valid positions
    
    # Identify valid positions and start/end points
    for r in range(R):
        for c in range(C):
            nbr = 0  # Count of valid neighbors
            
            # Check neighbors in four directions
            for ch, dr, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= r + dr < R and 0 <= c + dc < C and G[r + dr][c + dc] != '#'):
                    nbr += 1
            
            # Add position to valid set if it has more than two neighbors and is not a wall
            if nbr > 2 and G[r][c] != '#':
                V.add((r, c))
    
    # Identify start and end points in the grid
    for c in range(C):
        if G[0][c] == '.':
            V.add((0, c))
            start = (0, c)
        if G[R - 1][c] == '.':
            V.add((R - 1, c))
            end = (R - 1, c)

    # Create an adjacency list for valid positions
    E = {}
    for (rv, cv) in V:
        E[(rv, cv)] = []
        Q = deque([(rv, cv, 0)])  # Queue for BFS with (row, column, distance)
        SEEN = set()  # Set to track seen positions
        
        while Q:
            r, c, d = Q.popleft()
            if (r, c) in SEEN:
                continue
            
            SEEN.add((r, c))
            
            # If we find another valid position, add it to the adjacency list
            if (r, c) in V and (r, c) != (rv, cv):
                E[(rv, cv)].append(((r, c), d))
                continue
            
            # Explore neighbors in four directions
            for ch, dr, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= r + dr < R and 0 <= c + dc < C and G[r + dr][c + dc] != '#'):
                    if part1 and G[r][c] in ['<', '>', '^', 'v'] and G[r][c] != ch:
                        continue
                    Q.append((r + dr, c + dc, d + 1))

    count = 0
    ans = 0
    SEEN = [[False for _ in range(C)] for _ in range(R)]  # Track visited positions

    def dfs(v, d):
        nonlocal count
        nonlocal ans
        
        count += 1
        r, c = v
        
        if SEEN[r][c]:
            return
        
        SEEN[r][c] = True
        
        # Update answer if we reach the last row
        if r == R - 1:
            ans = max(ans, d)
        
        # Recursively visit connected nodes
        for (y, yd) in E[v]:
            dfs(y, d + yd)
        
        SEEN[r][c] = False
    
    dfs(start, 0)  # Start DFS from the starting point
    
    return ans

# Execute the solve function for both parts of the problem
print(solve(True))   # Solve part 1
print(solve(False))  # Solve part 2