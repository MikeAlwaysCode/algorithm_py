import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    nums = ints()
    ori = [0] * (n + 1)
    p = [0] * (n + 1)
    q = [0] * (n + 1)
    for _ in range(m):
        l, r, x = mint()
        if l == r:
            nums[l - 1] = x
        p[l - 1] += x
        p[r] -= x
        q[l - 1] += r - l + 1
        q[r] -= r - l + 1
        ori[l - 1] += r - l
        ori[r] -= r - l
    print(ori)
    print(p)
    print(q)
    ans = [0] * n
    curo = curp = curq = 0
    for i in range(n):
        curo += ori[i]
        curp += p[i]
        curq += q[i]
        if curq == 0:
            ans[i] = nums[i]
        else:
            ans[i] = (curo * nums[i] + curp) % MOD * pow(curq, MOD - 2, MOD) % MOD
    print(*ans)


solve()
