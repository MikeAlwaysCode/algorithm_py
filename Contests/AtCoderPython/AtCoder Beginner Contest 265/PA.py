from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

x, y, n = map(int, input().split())

ans = min(n // 3 * y, n // 3 * 3 * x) + (n % 3) * x
print(ans)