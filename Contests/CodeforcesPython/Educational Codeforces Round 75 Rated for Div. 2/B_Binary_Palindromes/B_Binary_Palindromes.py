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
    zero = one = odd = 0
    for _ in range(n):
        s = input()
        l = len(s)
        cnt = s.count('0')
        zero += cnt
        one += l - cnt
        odd += l & 1
    ans = n
    if odd == 0 and zero & 1:
        ans -= 1
    print(ans)


for _ in range(int(input())):
    solve()
