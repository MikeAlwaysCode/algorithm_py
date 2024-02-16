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
    s = [0] * 2
    for i, x in enumerate(nums):
        s[i & 1] += x
    if not n & 1:
        s[0], s[1] = s[1], s[0]
    print("Alice" if s[0] > s[1] else "Bob")

for _ in range(sint()):
    solve()
