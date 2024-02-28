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

def bit_count(x):
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x & 0x0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f)
    x = (x & 0x00ff00ff) + ((x >> 8) & 0x00ff00ff)
    x = (x & 0x0000ffff) + ((x >> 16) & 0x0000ffff)
    return x

# 横竖的1100，起点是0123，共8种形态
# 把坐标映射到起始点，看跟当前是否一样
def zz(i: int, j: int) -> int:
    return (i + j // 2) & 1

def solve() -> None:
    n, m, q = mint()
    print(8)
    mask = 0
    for _ in range(q):
        x, y, t = input().split()
        x, y = int(x), int(y)
        c = (t == "circle")
        for d in range(4):
            if zz(x, y + d) ^ c:
                mask |= 1 << d
            if zz(y, x + d) ^ c:
                mask |= 1 << (d + 4)
        print(8 - bit_count(mask))

for _ in range(int(input())):
    solve()
