from collections import Counter, defaultdict
import sys

n, l, r = map(int, input().split())
arr = list(map(int, input().split()))

s = [0] * (n+1)
for i in range(n-1, -1, -1):
    s[i] = min(s[i+1] + arr[i], r*(n-i))
# print(s)
ls = 0
ans = sys.maxsize
for i in range(0, n+1):
    ans = min(ans, ls + s[i])
    ls += l

print(ans)