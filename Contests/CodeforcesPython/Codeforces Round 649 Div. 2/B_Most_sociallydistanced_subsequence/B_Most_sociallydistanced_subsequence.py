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
    p = ints()
    ans = p[:2]
    for x in p[2:]:
        if (x > ans[-1]) == (ans[-1] > ans[-2]):
            ans[-1] = x
        else:
            ans.append(x)
    print(len(ans))
    print(*ans)


for _ in range(int(input())):
    solve()
