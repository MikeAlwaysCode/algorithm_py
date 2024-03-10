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
    n = sint()
    nums = ints()

    pre, nxt = dict(), dict()
    for i in range(n - 1):
        nxt[nums[i]] = nums[i + 1]
        pre[nums[i + 1]] = nums[i]
    
    pre[nums[0]] = 0
    nxt[0] = nums[0]
    pre[-1] = nums[-1]
    nxt[nums[-1]] = -1

    for _ in range(sint()):
        qry = ints()
        if qry[0] == 2:
            x = qry[1]
            nxt[pre[x]] = nxt[x]
            pre[nxt[x]] = pre[x]
            del pre[x]
            del nxt[x]
        else:
            x, y = qry[1], qry[2]
            nxt[y] = nxt[x]
            pre[nxt[x]] = y
            nxt[x] = y
            pre[y] = x

    cur = nxt[0]
    ans = []
    while cur != -1:
        ans.append(cur)
        cur = nxt[cur]
    print(*ans)

solve()
