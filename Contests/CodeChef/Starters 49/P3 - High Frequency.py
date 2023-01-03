from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    c = Counter(arr)
    # nc = Counter(c.values())
    ans = 0
    
    nclist = list(c.items())
    nclist.sort(key = lambda x:x[1])

    ans = ( nclist[-1][1] + 1 ) // 2
    if len(nclist) > 1: ans = max(ans, nclist[-2][1])
    
    # ans = ( count + time - 1 ) // time
    
    print(ans)