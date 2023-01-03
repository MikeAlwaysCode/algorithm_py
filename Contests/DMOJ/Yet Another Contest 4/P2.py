n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * (n+1)
count = [0] * (n+1)
pairs = [[] for _ in range(n+1)]
maxb = 0
for i, b in enumerate(arr):
    pairs[b].append(i+1)
    count[b] += 1
    maxb = max(maxb, b)
# print(pairs)
for i in pairs[1]:
    ans[i] = i
exist = True
idx2 = -1
if n >= 2:
    for i in pairs[2]:
        if pairs[1]:
            ans[i] = pairs[1][0]
        else:
            if idx2 != -1:
                ans[i] = idx2
                ans[idx2] = i
                idx2 = -1
            else:
                idx2 = i
if idx2 != -1:
    print(-1)
else:
    for i in range(3, maxb+1):
        if pairs[i-1]:
            for j in pairs[i]:
                ans[j] = pairs[i-1][0]
        elif count[i] % i != 0:
            exist = False
            break
        else:
            n = len(pairs[i])
            for j in range(n):
                k = (j+1) % i + j // i * i
                ans[pairs[i][j]] = pairs[i][k]
if not exist:
    print(-1)
else:
    print(*ans[1:])
# print(*ans)
'''
pairs = list(zip(arr, range(n)))
pairs.sort()
idx2 = -1
exist = True
for p in pairs:
    if p[0] == 1:
        ans[p[1]] = p[1] + 1
        d[p[0]] = p[1] + 1 # 1
    elif p[0] == 2:
        if idx2 != -1:
            ans[idx2] = p[1] + 1
            ans[p[1]] = idx2 + 1
            d[p[0]] = idx2 + 1
            idx2 = -1
        else:
            idx2 = p[1]
    else:
        if idx2 != -1:
            if d[1] >= 0: # 2不成对
                ans[idx2] = d[1]
                d[2] = idx2 + 1
                idx2 = -1
            else:
                exist = False
                break
        if d[p[0] - 1] < 0:
            exist = False
            break
        else:
            ans[p[1]] = d[p[0] - 1]
            d[p[0]] = p[1] + 1
# print(d)
if not exist:
    print(-1)
if idx2 != -1:
    if d[1] >= 0:
        ans[idx2] = d[1]
        print(*ans)
    else:
        print(-1)
else:
    print(*ans)
'''