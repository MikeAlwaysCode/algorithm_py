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
    n, k, sb, sc = mint()
    P = ints()
    A = ints()

    def get_score(x: int) -> int:
        res = ps = 0
        seen = [False] * n
        ck = k
        while not seen[x] and ck:
            res = max(res, ps + ck * A[x])
            ps += A[x]
            ck -= 1
            seen[x] = True
            x = P[x] - 1
        return res
    
    r1, r2 = get_score(sb - 1), get_score(sc - 1)
    print("Bodya" if r1 > r2 else "Sasha" if r1 < r2 else "Draw")


for _ in range(int(input())):
    solve()
