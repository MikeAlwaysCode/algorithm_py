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
    w_cnt = [[0] * 30 for _ in range(n + 1)]
    y_cnt = [[0] * 30 for _ in range(n + 1)]
    for i in range(n):
        x, y = mint()
        mask = (1 << (x ^ y).bit_length()) - 1
        cy = y & mask
        cw = y - cy
        for bit in range(29, -1, -1):
            w_cnt[i + 1][bit] = w_cnt[i][bit] + ((cw >> bit) & 1)
            y_cnt[i + 1][bit] = y_cnt[i][bit] + ((cy >> bit) & 1)

    ans = []
    for _ in range(sint()):
        l, r = mint()
        l -= 1
        x = 0
        for bit in range(29, -1, -1):
            if w_cnt[r][bit] - w_cnt[l][bit] or y_cnt[r][bit] - y_cnt[l][bit]:
                x |= 1 << bit
                if y_cnt[r][bit] - y_cnt[l][bit] - 1 + int(w_cnt[r][bit] - w_cnt[l][bit] > 0):
                    x |= (1 << bit) - 1
                    break
        ans.append(x)
    print(*ans)

for _ in range(int(input())):
    solve()
