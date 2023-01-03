from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

n = int(input())
ans = 3.5
for i in range(1, n):
    tmp = 0
    for d in range(1, 7):
        tmp += max(ans, d) / 6
    ans = tmp
print("{:.6f}".format(ans))