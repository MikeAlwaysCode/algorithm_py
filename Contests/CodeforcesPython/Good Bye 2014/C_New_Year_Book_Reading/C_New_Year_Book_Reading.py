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
    vals = ints()
    books = ints()
    ans = 0
    last = [0] * n
    seen = [-1] * n
    for i, b in enumerate(books):
        b -= 1
        for j in range(last[b], i):
            if seen[books[j] - 1] != b:
                ans += vals[books[j] - 1]
                seen[books[j] - 1] = b
        seen[b] = b
        last[b] = i + 1
    print(ans) 


solve()
