from collections import Counter, defaultdict
import math
# from sortedcontainers import SortedSet, SortedList

vertices = []
for _ in range(4):
    x, y = map(int, input().split())
    vertices.append((x, y))

chk = True
for i in range(4):
    dx1 = vertices[i][0] - vertices[i-1][0]
    dy1 = vertices[i][1] - vertices[i-1][1]
    dx2 = vertices[(i+1)%4][0] - vertices[i][0]
    dy2 = vertices[(i+1)%4][1] - vertices[i][1]
    angle1 = int(math.atan2(dy1, dx1) * 180 / math.pi)
    angle2 = int(math.atan2(dy2, dx2) * 180 / math.pi)
    inside = angle2 - angle1
    if inside < 0:
        inside += 360
    if inside >= 180:
        chk = False
        break

print("Yes" if chk else "No")