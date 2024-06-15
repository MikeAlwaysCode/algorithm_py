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

mxn = 10 ** 6
factor = [1] * (mxn + 1)
primes = list()
for i in range(2, mxn + 1):
    if factor[i] != 1:
        continue
    primes.append(i)
    for j in range(i, mxn + 1, i):
        factor[j] = i

def solve() -> None:
    n = sint()

    if n == 2:
        print(1, 1)
        return
    
    def check(x: int) -> bool:
        if x & 1:
            return x + 1 + x * (x - 1) // 2 >= n
        else:
            return x * (x - 1) // 2 - x // 2 + 2 + x >= n
        
    l, r = 1, 10000
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
            
    # 半欧拉图, 恰有两个奇数度顶点, 存在欧拉路径
    k = 0
    g = [[] for _ in range(r)]
    for i in range(r):
        for j in range(i + 1, r):
            if not r & 1 and i & 1 and i + 1 == j:
                continue
            g[i].append((j, k))
            g[j].append((i, k))
            k += 1
    # print(g)
    res = []
    stk = [0]
    seen = [False] * k
    while stk:
        if g[stk[-1]]:
            v, e = g[stk[-1]].pop()
            if seen[e]:
                continue
            seen[e] = True
            stk.append(v)
        else:
            res.append(primes[stk.pop()])
            res.append(res[-1])
    res.reverse()
    print(*res[:n])


for _ in range(int(input())):
    solve()
