import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    g = []
    for _ in range(3):
        g.append(ints())
    pw3 = [1] * 10
    for i in range(1, 10):
        pw3[i] = pw3[i - 1] * 3
    mx = pw3[-1]
    dp = [-1] * mx
    def check(mask: int) -> int:
        row = [[0] * 2 for _ in range(3)]
        col = [[0] * 2 for _ in range(3)]
        dia1 = [0] * 2
        dia2 = [0] * 2
        cnt = [0] * 2
        score = [0] * 2
        for bit in range(9):
            mask, x = divmod(mask, 3)
            if x == 0:
                continue
            x -= 1
            i, j = divmod(bit, 3)
            row[i][x] += 1
            col[j][x] += 1
            cnt[x] += 1
            score[x] += g[i][j]
            if i == j:
                dia1[x] += 1
            if i + j == 2:
                dia2[x] += 1
        if not (cnt[1] == cnt[0] or cnt[1] - cnt[0] == 1):
            return -1
        t = a = False
        for d in range(3):
            if row[d][1] == 3 or col[d][1] == 3:
                t = True
            if row[d][0] == 3 or col[d][0] == 3:
                a = True
        if dia1[1] == 3 or dia2[1] == 3:
            t = True
        if dia1[0] == 3 or dia2[0] == 3:
            a = True
        if t and a:
            return -1
        if t:
            return 1
        elif a:
            return 0
        if cnt[1] != 5:
            return -1
        return 1 if score[1] > score[0] else 0
    for mask in range(mx - 1, 0, -1):
        res = check(mask)
        if res != -1:
            dp[mask] = res
        
        if dp[mask] == -1:
            continue
        
        cnt = [0] * 2
        nmask = mask
        for bit in range(9):
            nmask, x = divmod(nmask, 3)
            if x == 0:
                continue
            cnt[x - 1] += 1

        nxt = 2 if cnt[1] > cnt[0] else 1
        nmask = mask
        for bit in range(9):
            nmask, x = divmod(nmask, 3)
            if x != nxt:
                continue
            vmask = mask - x * pw3[bit]
            if dp[vmask] == -1 or (x == 2 and dp[mask] == 1) or (x == 1 and dp[mask] == 0):
                dp[vmask] = dp[mask]
    print("Takahashi" if dp[0] else "Aoki")

solve()
