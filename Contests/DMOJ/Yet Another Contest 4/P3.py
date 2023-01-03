n, m, b = map(int, input().split())
edges = list()
for _ in range(m):
    x, y = map(int, input().split())
    edges.append((x, y))

v = 1 << (len(bin(b)) - 3)