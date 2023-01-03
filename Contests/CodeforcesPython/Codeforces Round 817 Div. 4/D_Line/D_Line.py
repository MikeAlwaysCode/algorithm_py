def solve() -> None:
    n = int(input())
    s = str(input())

    ans = [0] * n
    tot = 0
    v = []
    for i in range(n):
        if s[i] == 'L':
            v.append(max(0, (n-i-1)-i))
            tot += i
        else:
            v.append(max(0, i-(n-i-1)))
            tot += n - i - 1
    v.sort(reverse=True)
    for i in range(n):
        tot += v[i]
        ans[i] = tot
    print(*ans)
    '''
    ls = [i for i in range(n)]
    rs = [i for i in range(n-1, -1, -1)]

    ans = [0] * (n + 1)
    for i, x in enumerate(s):
        if x == 'L':
            ans[0] += ls[i]
        else:
            ans[0] += rs[i]
    
    l = 0
    r = n - 1
    # print(*ans)
    # print(l, r)
    k = 1
    while k <= n:
        while l <= r and s[l] == 'R' and s[r] == 'L':
            l += 1
            r -= 1

        if l >= r:
            ans[k] = ans[k-1]
            k += 1
        else:
            if s[l] == 'L':
                ans[k] = ans[k-1] + rs[l] - ls[l]
                k += 1

            if s[r] == 'R':
                ans[k] = ans[k-1] + ls[r] - rs[r]
                k += 1
            l += 1
            r -= 1
        
    print(*ans[1:])
    '''
t = int(input())
for _ in range(t):
    solve()