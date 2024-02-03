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
    m = sint()
    B = ints()
    
    A.sort()
    B.sort()
    ans = i = j = 0
    while i < n and j < m:
        if abs(A[i] - B[j]) <= 1:
            ans += 1
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

    return


solve()
