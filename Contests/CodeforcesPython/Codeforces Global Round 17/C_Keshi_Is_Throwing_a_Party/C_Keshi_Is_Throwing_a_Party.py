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
    p = []
    for _ in range(n):
        p.append(tuple(mint()))

    def check(x: int) -> bool:
        cnt = 0
        for a, b in p:
            if cnt <= b and x - 1 - cnt <= a:
                cnt += 1
                if cnt == x:
                    break
        return cnt >= x
    
    l, r = 1, n
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)


for _ in range(int(input())):
    solve()
