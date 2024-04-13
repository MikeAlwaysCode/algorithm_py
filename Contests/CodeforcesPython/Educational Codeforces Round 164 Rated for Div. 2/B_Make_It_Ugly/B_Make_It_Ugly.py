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
    pos = [i for i in range(n) if nums[i] != nums[0]]
    if not pos:
        print(-1)
        return
    ans = min(pos[0], n - 1 - pos[-1])
    for i in range(1, len(pos)):
        ans = min(ans, pos[i] - pos[i - 1] - 1)
    print(ans)


for _ in range(int(input())):
    solve()
