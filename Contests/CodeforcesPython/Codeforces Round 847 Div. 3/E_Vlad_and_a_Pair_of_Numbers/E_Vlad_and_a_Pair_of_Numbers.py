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
    x = int(input())
    if x & 1:
        print(-1)
        return
    a, b  = x, x // 2
    if a & b:
        print(-1)
        return
    a |= b

    '''
    a = b = 0
    pre = True
    bit = 0
    while x:
        if x & 1:
            if pre:
                print(-1)
                return
            pre = True
            a |= (1 << bit) + (1 << (bit - 1))
            b |= 1 << (bit - 1)
        else:
            pre = False
        x >>= 1
        bit += 1
    '''

    print(a, b)


for _ in range(int(input())):
    solve()
