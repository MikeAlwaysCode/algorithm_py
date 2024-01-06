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
    n, k = mint()
    A = ints()
    B = ints()
    idx = sorted(range(n), key = lambda x: A[x])
    ans = [0] * n
    B.sort()
    for i in range(k):
        if A[idx[n - k + i]] <= B[i]:
            print("NO")
            return
        ans[idx[n - k + i]] = B[i]
    for i in range(k, n):
        if A[idx[i - k]] > B[i]:
            print("NO")
            return
        ans[idx[i - k]] = B[i]
    print("YES")
    print(*ans)


for _ in range(int(input())):
    solve()
