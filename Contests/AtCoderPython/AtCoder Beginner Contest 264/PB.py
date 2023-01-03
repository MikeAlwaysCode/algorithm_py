from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

r, c = map(int, input().split())

if r&1:
    ans = "black"
    k = min(r // 2, (15-r)//2)
    if not c&1 and ( c // 2 <= k or c // 2 > 8 - k ):
        ans = "white"
else:
    ans = "white"
    k = min(r // 2, (16-r)//2)
    if c&1 and ( c // 2 < k or c // 2 >= 8 - k ):
        ans = "black"

print(ans)