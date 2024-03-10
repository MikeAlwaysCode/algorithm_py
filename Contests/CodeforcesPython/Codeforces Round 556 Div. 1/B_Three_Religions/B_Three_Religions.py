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
    n, q = mint()
    s = input()

    nxt = [[n] * 26 for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            nxt[i][j] = nxt[i + 1][j]
        nxt[i][ord(s[i]) - 97] = i

    m = 255
    def encode(mask: list):
        return (mask[0] * m + mask[1]) * m + mask[2]
    
    # def decode(x: int):
    #     xy, z = divmod(x, m)
    #     return *divmod(xy, m), z

    dp = [n] * (m ** 3)
    dp[0] = -1

    cur = [0] * 3
    s = [[] for _ in range(3)]

    for _ in range(q):
        qry = input().split()
        idx = int(qry[1]) - 1
        if qry[0] == '-':
            s[idx].pop()
            cur[idx] -= 1
        else:
            c = ord(qry[2]) - 97

            mask = [0, 0, 0]
            mask[idx] = cur[idx] + 1
            for i in range(cur[(idx + 1) % 3] + 1):
                for j in range(cur[(idx + 2) % 3] + 1):
                    mask[(idx + 1) % 3] = i
                    mask[(idx + 2) % 3] = j
                    pmask = mask[:]
                    pmask[idx] -= 1
                    dp[encode(mask)] = nxt[dp[encode(pmask)] + 1][c]
                    if i:
                        pmask = mask[:]
                        pmask[(idx + 1) % 3] -= 1
                        if nxt[dp[encode(pmask)] + 1][s[(idx + 1) % 3][i - 1]] < dp[encode(mask)]:
                            dp[encode(mask)] = nxt[dp[encode(pmask)] + 1][s[(idx + 1) % 3][i - 1]]
                    if j:
                        pmask = mask[:]
                        pmask[(idx + 2) % 3] -= 1
                        if nxt[dp[encode(pmask)] + 1][s[(idx + 2) % 3][j - 1]] < dp[encode(mask)]:
                            dp[encode(mask)] = nxt[dp[encode(pmask)] + 1][s[(idx + 2) % 3][j - 1]]

            s[idx].append(c)
            cur[idx] += 1
        
        print('YES' if dp[encode(cur)] < n else 'NO')

solve()
