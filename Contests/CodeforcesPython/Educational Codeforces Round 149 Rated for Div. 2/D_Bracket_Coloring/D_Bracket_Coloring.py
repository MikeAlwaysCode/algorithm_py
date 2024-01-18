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
    s = input()

    if n & 1:
        print(-1)
        return

    k = 1
    ans = [1] * n

    cur = 0
    p = 1
    t = 1 if s[0] == "(" else -1
    for i, c in enumerate(s):
        if c == "(":
            cur += 1
        else:
            cur -= 1
        
        if cur * t < 0:
            t = - t
            p ^= 3
            if k == 1: k += 1
        
        ans[i] = p
    
    if cur != 0:
        print(-1)
    else:
        print(k)
        print(*ans)


for _ in range(int(input())):
    solve()
