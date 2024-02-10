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
    A = ints()
    B = ints()

    ans = [n, 0]
    # min
    for i in range(3):
        ta, tb = A[:], B[:]
        for j in range(3):
            m = min(ta[(i + j) % 3], tb[(i + j - 1) % 3])
            ta[(i + j) % 3] -= m
            tb[(i + j - 1) % 3] -= m
            m = min(ta[(i + j) % 3], tb[(i + j) % 3])
            ta[(i + j) % 3] -= m
            tb[(i + j) % 3] -= m
        ans[0] = min(ans[0], sum(ta))
    
    # max
    for i in range(3):
        ans[1] += min(A[(i + j) % 3], B[(i + j + 1) % 3])

    print(*ans)


solve()
