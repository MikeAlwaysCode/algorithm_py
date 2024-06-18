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
    if k & 1:
        print("No")
        return
    mx = ((n & 1 ^ 1) + n - 1) * ((n + 1) // 2)
    if k > mx:
        print("No")
        return
    ans = list(range(1, n + 1))
    k //= 2
    i, j = 0, n - 1
    while k:
        m = min(k, j - i)
        j = i + m
        ans[i], ans[j] = ans[j], ans[i]
        i += 1
        j -= 1
        k -= m
    print("Yes")
    print(*ans)


for _ in range(int(input())):
    solve()