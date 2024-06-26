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
    s = input()
    cnt = [0] * n
    for i, c in enumerate(s):
        cnt[i] = 1 if c == 'W' else -1
    
    for i in range(n - 2, -1, -1):
        cnt[p[i] - 1] += cnt[i + 1]

    print(sum(v == 0 for v in cnt))


for _ in range(int(input())):
    solve()
