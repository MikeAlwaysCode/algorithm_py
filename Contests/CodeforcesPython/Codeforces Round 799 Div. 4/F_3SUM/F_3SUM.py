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
    seen1 = [False] * 10
    seen2 = [False] * 10
    for x in nums:
        x %= 10
        if seen2[(3 - x) % 10]:
            print("YES")
            return
        for y, v in enumerate(seen1):
            if v:
                seen2[(x + y) % 10] = True
        seen1[x] = True
    print("NO")


for _ in range(int(input())):
    solve()
