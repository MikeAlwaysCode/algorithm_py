import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    ans = set()
    row = [0] * (n + 1)
    col = [0] * (n + 1)
    for _ in range(m):
        a, b = mint()
        row[a] += 1
        col[b] += 1
        ans.add((a, b))
    
    s = set()
    for j in range(1, n + 1):
        if col[j] < m:
            s.add(j)
            
    ns = set()
    for i in range(1, n):
        while row[i] < m:
            j = s.pop()
            if (i, j) in ans:
                ns.add(j)
                continue
            row[i] += 1
            col[j] += 1
            ans.add((i, j))
            if col[j] < m:
                ns.add(j)
        s |= ns
        ns = set()
    print(s)
    print(len(ans))
    for a, b in ans:
        print(a, b)


solve()
