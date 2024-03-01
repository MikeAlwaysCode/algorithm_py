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
    s = input()
    n = len(s)
    cnt0 = s.count('0')
    cnt1 = n - cnt0
    for i, c in enumerate(s):
        if c == '0':
            cnt1 -= 1
        else:
            cnt0 -= 1
        if cnt0 < 0 or cnt1 < 0:
            print(n - i)
            return
    print(0)


for _ in range(int(input())):
    solve()
