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
    s = m1 = 0
    for x in nums:
        s = (s + x) % 3
        if x % 3 == 1:
            m1 = 1
    if s == 0:
        print(0)
    elif s == 2 or (s == 1 and m1):
        print(1)
    else:
        print(2)


for _ in range(int(input())):
    solve()
