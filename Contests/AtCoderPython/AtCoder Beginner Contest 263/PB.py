from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

N = int(input())
arr = list(map(int, input().split()))

ans = 0
i = N - 2
while i >= 0:
    i = arr[i]
    ans += 1
    if i == 1:
        break
    i -= 2
print(ans)