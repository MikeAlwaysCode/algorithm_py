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
    nums = ints()
    bit = [[0] * 2 for _ in range(n + 1)]
    
    def query(x: int) -> tuple:
        res1 = res2 = 0
        while x:
            res1 += bit[x][0]
            res2 += bit[x][1]
            x &= x - 1
        return (res1, res2)

    def add(x: int, val: int):
        while x <= n:
            bit[x][0] += 1
            bit[x][1] += val
            x += x & -x
    
    ans0 = ans1 = 0
    for i, x in enumerate(nums, 1):
        ans0 += i * (n - i + 1) * (n - i)
        r1, r2 = query(x)
        s1, s2 = query(n)
        ans1 += (s1 - r1) * n * (n + 1) - (s2 - r2) * 2 * (n - i + 1)
        add(x, i)

    ans = ans0 / (2 * n * (n + 1)) + ans1 / (n * (n + 1))
    print(ans)

solve()
