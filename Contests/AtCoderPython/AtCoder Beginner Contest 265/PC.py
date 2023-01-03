from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

dir = {'U':(-1, 0), 'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())
visit = [[False] * w for _ in range(h)]
i, j = 0, 0
inf = False
while True:
    ni = i + dir[grid[i][j]][0]
    nj = j + dir[grid[i][j]][1]
    if ni < 0 or ni >= h or nj < 0 or nj >= w:
        break
    if visit[ni][nj]:
        inf = True
        break
    i, j = ni, nj
    visit[i][j] = True

if inf:
    print(-1)
else:
    print(i+1, j+1)