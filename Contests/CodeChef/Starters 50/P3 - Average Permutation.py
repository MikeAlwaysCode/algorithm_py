from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    '''
    ans = [i for i in range(-1, n-1)]
    if n == 3:
        ans[0] = n
        ans[1] = n - 1
    else:
        ans[0] = n
        ans[1] = n - 2
        ans[n-2] = n - 3
        ans[n-1] = n - 1
    '''
    ans = [0] * n
    s, e = 0, n-1
    cnt = n
    while s < e:
        ans[s] = cnt
        ans[e] = cnt-1
        cnt -= 2
        s += 1
        e -= 1
    if n & 1:
        ans[s] = cnt
    print(*ans)

t = int(input())
for _ in range(t):
    solve()