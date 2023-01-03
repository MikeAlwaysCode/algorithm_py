from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

n, m, t = map(int, input().split())
arr = list(map(int, input().split()))
b = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    b[x-1] = y

idx = 0
while idx < n - 1:
    t += b[idx] - arr[idx]
    if t <= 0:
        break
    idx += 1

print("Yes" if idx == n - 1 else "No")