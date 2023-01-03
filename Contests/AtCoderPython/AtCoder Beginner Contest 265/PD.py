from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

n, p, q, r = map(int, input().split())
arr = list(map(int, input().split()))

s = {0}
tot = 0
for a in arr:
    tot += a
    s.add(tot)

for x in s:
    if x + p in s and x + p + q in s and x + p + q + r in s:
        print("Yes")
        exit()
print("No")

'''
cnt = [0] * (n + 1)
for i in range(n):
    cnt[i+1] = cnt[i] + arr[i]

i, j = 0, 1
# j: n-2, k: n-1, l: n
while j < n - 1:
    while j < n - 1 and cnt[j] - cnt[i] != p:
        if cnt[j] - cnt[i] > p and i < j:
            i += 1
        else:
            j += 1
    if j >= n - 1 or cnt[j] - cnt[i] != p:
        # p not found
        break
    
    k = j + 1
    while k < n and cnt[k] - cnt[j] < q:
        k += 1
    
    if k >= n or cnt[k] - cnt[j] != q:
        # q not found
        i += 1
        j += 1
        continue

    l = k + 1
    while l <= n and cnt[l] - cnt[k] < r:
        l += 1

    if l <= n and cnt[l] - cnt[k] == r:
        chk = True
        break
    else:
        i += 1
        j += 1
        
    k, l = j+1, n
    while k < l and cnt[k] - cnt[j] != q and cnt[l] - cnt[k] != r:
        if cnt[k] - cnt[j] < q:
            k += 1
        elif cnt[k] - cnt[j] > q:
            break
        if cnt[l] - cnt[k] > r:
            l -= 1
    
    if k < n and l <= n and cnt[k] - cnt[j] == q and cnt[l] - cnt[k] == r:
        print("Yes")
        exit()
    else:
        i += 1
        j += 1

print("No")
'''