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
    n, k = mint()
    nums = ints()
    pos = [[] for _ in range(n + 1)]
    for i, x in enumerate(nums):
        pos[x].append(i)
    l, r = [], []
    bothl = []
    bothr = []
    for x in range(1, n + 1):
        if (pos[x][0] < n) != (pos[x][1] < n):
            l.append(x)
            r.append(x)
        elif pos[x][0] < n:
            bothl.append(x)
        else:
            bothr.append(x)
        if len(l) == k * 2 or len(l) + min(len(bothl), len(bothr)) * 2 >= k * 2:
            break
    if (k * 2 - len(l)) & 1:
        l.pop()
        r.pop()
    while len(l) < k * 2:
        l.append(bothl.pop())
        l.append(l[-1])
        r.append(bothr.pop())
        r.append(r[-1])

    print(*l)
    print(*r)

for _ in range(int(input())):
    solve()
