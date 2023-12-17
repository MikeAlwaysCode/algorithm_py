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
    pos = sint()
    stk = []
    n = len(s)
    for i, c in enumerate(s):
        if pos <= n:
            stk.append(s[i:])
            break
        while stk and stk[-1] > c:
            stk.pop()
            pos -= n
            n -= 1
            if pos <= n: break
        if pos <= n:
            stk.append(s[i:])
            break
        stk.append(c)
    
    ans = "".join(stk)
    i = n - 1
    while pos > i + 1:
        pos -= i + 1
        i -= 1
    
    print(ans[pos - 1], end = "")


for _ in range(int(input())):
    solve()

    