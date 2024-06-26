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

    for i in range(n):
        if A[i] > B[i]:
            print("No")
            return
            
        if A[i] != B[i] and B[(i + 1) % n] < B[i] - 1:
            print("No")
            return

    print("Yes")

for _ in range(int(input())):
    solve()