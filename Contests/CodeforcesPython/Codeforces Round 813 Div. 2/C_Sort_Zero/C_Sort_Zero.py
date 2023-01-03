def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    
    chk = [False] * (n+1)
    s = set()
    for i in range(1, n):
        x = arr[i]
        if chk[x]:
            x = 0
            chk[arr[i-1]] = True
            for d in s:
                chk[d] = True
            s.clear()
            continue

        p = arr[i-1]
        if chk[p]:
            continue

        if x < p:
            chk[p] = True
            for d in s:
                chk[d] = True
            s.clear()
        else:
            s.add(p)
    # print(chk)
    print(sum(x for x in chk))

t = int(input())
for _ in range(t):
    solve()