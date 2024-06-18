import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    s = input()
    t = input()
    
    bit = [0] * (n + 1)

    def query(x: int) -> int:
        res = 0
        while x:
            res += bit[x]
            x &= x - 1
        return res

    def add(x: int, val: int):
        while x <= n:
            bit[x] += val
            x += x & -x
    
    seg = []
    for i in range(n):
        if s[i] == '1':
            seg.append((i + 1, i + 1))
            add(i + 1, 1)
        else:
            l = r = -1
            if i > 0 and t[i - 1] == '1':
                l = i - 1
            elif i > 1 and s[i - 2] == '0':
                l = i - 2
            if i < n - 1 and t[i + 1] == '1':
                r = i + 1
            elif i < n - 2 and s[i + 2] == '0':
                r = i + 2
            if l != -1 and r != -1:
                seg.append((l + 1, r + 1))
                add(r + 1, 1)
    
    q = sint()
    qry = []
    for i in range(q):
        l, r = mint()
        qry.append((l, r, i))

    ans = [0] * q
    qry.sort()
    seg.sort()
    j = 0
    for l, r, i in qry:
        while j < len(seg) and seg[j][0] < l:
            add(seg[j][1], -1)
            j += 1
        ans[i] = query(r)
    
    print(*ans, sep='\n')


for _ in range(int(input())):
    solve()
