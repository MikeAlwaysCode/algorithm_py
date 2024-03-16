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
    s = mx = zero = 0
    for a in nums:
        if a == 0:
            zero += 1
        else:
            s += zero
            mx = max(mx, zero)
            zero = 0
    s += zero
    mx = max(mx, zero)
    if mx * 2 > s:
        ans = s - mx
    else:
        ans = s // 2
    print(ans)


for _ in range(int(input())):
    solve()