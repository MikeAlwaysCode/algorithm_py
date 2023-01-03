from collections import Counter, defaultdict
from math import factorial
# from sortedcontainers import SortedSet, SortedList

N = int(input())
arr = list(map(int, input().split()))

match, ans = 0, 0
for i in range(N):
    if arr[i] == i + 1:
        match += 1
    elif arr[i] > i + 1 and arr[arr[i]-1] == i + 1:
        ans += 1

if match >= 2:
    # ans += int(factorial(match) / (2 * factorial(match - 2)))
    ans += int(match * ( match - 1 ) / 2)

print(ans)