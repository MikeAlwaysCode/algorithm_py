from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

Y = int(input())
ans = Y // 4 * 4 + 2
if ans < Y: ans += 4
    
print(ans)