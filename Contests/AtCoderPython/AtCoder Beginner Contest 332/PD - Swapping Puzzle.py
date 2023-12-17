import math
import sys
from itertools import permutations

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
    n, m = mint()
    A = []
    for _ in range(n):
        A.append(ints())
    B = []
    for _ in range(n):
        B.append(ints())
    ans = math.inf

    def get_ops(per: tuple) -> int:
        res = 0
        for i, x in enumerate(per):
            for j in range(i + 1, len(per)):
                if per[j] < x:
                    res += 1
        return res

    def check(row: tuple, col: tuple) -> bool:
        for bi, ai in enumerate(row):
            for bj, aj in enumerate(col):
                if A[ai][aj] != B[bi][bj]:
                    return False
        return True

    for row in permutations(range(n)):
        ro = get_ops(row)

        for col in permutations(range(m)):
            if check(row, col):
                # print(row, col)
                ans = min(ans, ro + get_ops(col))

    print(-1 if ans == math.inf else ans)


solve()
