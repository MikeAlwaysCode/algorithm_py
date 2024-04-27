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
    if n == 1:
        print(k)
    else:
        a = b = 0
        last = -1
        for bit in range(31):
            if (k >> bit) & 1:
                if bit == last + 1:
                    a |= 1 << bit
                    last = bit
                else:
                    b |= 1 << (last + 1)
                    a |= (1 << bit) - (1 << (last + 1))
                    last = bit - 1
        ans = [a, b] + [0] * (n - 2)
        print(*ans)


for _ in range(int(input())):
    solve()
