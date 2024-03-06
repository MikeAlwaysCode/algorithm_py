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
    input()
    m, n = mint()
    fst = [0] * n
    sec = [0] * n
    for _ in range(m):
        p = ints()
        mx = cnt = 0
        for i, x in enumerate(p):
            fst[i] = max(fst[i], x)
            if x > mx:
                mx, cnt = x, 1
            elif x == mx:
                cnt += 1
        
        for i, x in enumerate(p):
            if cnt > 1 or x < mx:
                sec[i] = max(sec[i], x)
                
    print(min(min(fst), max(sec)))


for _ in range(int(input())):
    solve()
