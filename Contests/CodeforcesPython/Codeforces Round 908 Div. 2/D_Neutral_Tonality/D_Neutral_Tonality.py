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
    A = ints()
    B = ints()
    ans = []
    B.sort(reverse=True)
    j = 0
    for a in A:
        while j < m and B[j] >= a:
            ans.append(B[j])
            j += 1
        ans.append(a)
    ans.extend(B[j:])
    print(*ans)


for _ in range(int(input())):
    solve()
