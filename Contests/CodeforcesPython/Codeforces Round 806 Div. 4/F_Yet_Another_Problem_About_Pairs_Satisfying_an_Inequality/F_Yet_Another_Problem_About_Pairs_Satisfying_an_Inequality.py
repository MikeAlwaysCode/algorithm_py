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

    bit = [0] * (n + 1)

    def add(x: int, val: int) -> None:
        while x <= n:
            bit[x] += val
            x += x & -x

    def query(x: int) -> int:
        res = 0
        while x > 0:
            res += bit[x]
            x &= x - 1
        return res
    
    ans = 0
    for i, x in enumerate(nums, 1):
        if i > x:
            ans += query(x - 1)
            add(i, 1)
    
    print(ans)


for _ in range(int(input())):
    solve()
