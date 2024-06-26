import sys
from bisect import bisect_left

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
    n = int(input())
    arr = ints()

    ans = 2
    cnt = 0
    for i in range(1, n):
        cnt += 1
        if arr[i] == arr[i - 1]:
            continue
        j = i
        while j < n:
            cnt += 1
            j = bisect_left(arr, arr[j] * 2 - arr[i - 1], j + 1)

        ans = max(ans, cnt)
        cnt = 0
    ans = max(ans, cnt + 1)

    print(n - ans)

for _ in range(int(input())):
    solve()