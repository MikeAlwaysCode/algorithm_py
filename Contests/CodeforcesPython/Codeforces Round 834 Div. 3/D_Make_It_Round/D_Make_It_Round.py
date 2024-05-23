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
    n, m = mint()
    cnt = 0
    x = n
    while x % 10 == 0:
        x //= 10
    while x % 2 == 0:
        cnt += 1
        x //= 2
    while x % 5 == 0:
        cnt -= 1
        x //= 5
    p = 1
    if cnt > 0:
        while cnt and p * 5 <= m:
            p *= 5
            cnt -= 1
    elif cnt < 0:
        while cnt and p * 2 <= m:
            p *= 2
            cnt += 1

    while p * 10 <= m:
        p *= 10
    q = m // p
    ans = n * p * q
    print(ans)



for _ in range(int(input())):
    solve()
