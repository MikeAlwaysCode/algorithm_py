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
    cnt = bin(n)[2:].count('1')
    if cnt & 1:
        print("second", flush=True)
    else:
        print("first", flush=True)
        high = n.bit_length() - 1
        x = 1 << high
        y = n ^ x
        print(x, y, flush=True)
    while True:
        x, y = mint()
        if x == y == 0:
            return
        cnt1 = bin(x)[2:].count('1')
        if not cnt1 & 1:
            n = x
        else:
            n = y
        high = n.bit_length() - 1
        x = 1 << high
        y = n ^ x
        print(x, y, flush=True)


for _ in range(int(input())):
    solve()
