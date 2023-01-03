from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

n, m = map(int, input().split())
ans = [0] * n
def go(k, s):
    if k == n:
        print(*ans)
    else:
        for l in range(s, m+1):
            ans[k] = l
            go(k+1, l+1)
go(0, 1)

'''
arr = [i+1 for i in range(m)]
ans = [0] * n

def go(k, sPos, ePos):
    # print("==", k, sPos, ePos, arr[sPos], arr[ePos])
    cur = sPos
    while cur <= ePos:
        ans[k] = arr[cur]
        if k == n-1:
            print(*ans)
        else:
            go(k+1, cur + 1, m-n+1+k)
        cur += 1

for i in range(0, m-n+1):
    # first sequence
    ans = arr[i:i+n]
    print(*ans)

    if i == m - n:
        break
    
    for j in range(n-1, 0, -1):
        go(j, i + j + 1, m - n + j)
'''