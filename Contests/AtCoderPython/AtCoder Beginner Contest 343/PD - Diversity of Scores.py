import sys
from collections import Counter

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, t = mint()
    score = [0] * n
    cnt = Counter()
    cnt[0] = n
    for _ in range(t):
        i, x = mint()
        i -= 1
        cnt[score[i]] -= 1
        if cnt[score[i]] == 0:
            del cnt[score[i]]
        score[i] += x
        cnt[score[i]] += 1
        print(len(cnt))


solve()
