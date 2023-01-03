from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

l = len(bin(arr[0])) - 2
v = [0] * n
ans = 0

for i in range(1, l+1):
    b = (1<<i) - 1
    for j in range(n):
        v[j] = arr[j] & b
    v.sort(reverse=True)

    tot = sum(v[:k])
    chk = False
    if tot + m >= v[0] * k:
        chk = True
    else:
        for j in range(k, n):
            tot += v[j] - v[j-k]
            if tot + m >= v[j-k+1] * k:
                chk = True
                break
    if chk:
        ans = max(ans, (tot + m) // k)

print(ans)
