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

    if n == k:
        print("YES")
        print(1)
        print(1)
    elif n < k or n + 1 < k * 2:
        print("NO")
        return
    else:
        print("YES")
        print(2)
        print(n - k + 1, 1) 


for _ in range(int(input())):
    solve()
