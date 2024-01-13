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
    stk = []
    for x in nums:
        while stk and abs(stk[-1] - x) == 1:
            x = min(stk[-1], x)
            stk.pop()
        stk.append(x)
    print("YES" if len(stk) == 1 and stk[-1] == 0 else "NO")


for _ in range(int(input())):
    solve()