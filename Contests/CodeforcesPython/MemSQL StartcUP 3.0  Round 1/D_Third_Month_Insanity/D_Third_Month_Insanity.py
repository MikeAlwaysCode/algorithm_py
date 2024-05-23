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
    g = []
    for _ in range(1 << n):
        g.append(ints())
    
    prob = [1] * (1 << n)
    dp = [0] * (1 << n)

    for i in range(n):
        nprob = [0] * (1 << n)
        ndp = [0] * (1 << n)

        for j in range(0, 1 << n, 1 << i + 1):
            for k in range(j, j + (1 << i)):
                for nk in range(j + (1 << i), j + (1 << i + 1)):
                    nprob[k] += prob[k] * prob[nk] * g[k][nk] / 100
                    nprob[nk] += prob[k] * prob[nk] * g[nk][k] / 100
                    ndp[k] = max(ndp[k], dp[nk])
                    ndp[nk] = max(ndp[nk], dp[k])

        for j in range(1 << n):
            ndp[j] += nprob[j] * (1 << i) + dp[j]

        prob = nprob
        dp = ndp
    
    print(max(dp))


solve()
