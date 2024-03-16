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
    if n & 1:
        print("NO")
        return
    ans = []
    for i in range(n // 2):
        if i & 1:
            ans.append("BB")
        else:
            ans.append("AA")
    print("YES")
    print("".join(ans))


for _ in range(int(input())):
    solve()
