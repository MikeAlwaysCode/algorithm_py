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
    n, m = mint()
    pair = list(tuple(mint()) for _ in range(m))
    
    def check(x: int) -> bool:
        both = [0] * (n + 1)
        cnt = [0] * (n + 1)
        for a, b in pair:
            cnt[a] += 1
            cnt[b] += 1
            if a == x:
                both[b] += 1
            if b == x:
                both[a] += 1
        if cnt[x] >= m:
            return True
        for y in range(n + 1):
            if y == x: continue
            if cnt[x] + cnt[y] - both[y] >= m:
                return True
        return False
    
    print("YES" if check(pair[0][0]) or check(pair[0][1]) else "NO")

solve()