import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    s = input()
    t = input()
    lt = gt = False
    q = same = 0
    for a, b in zip(s, t):
        if a == '?' and b =='?':
            q += 2
            same += 1
        elif a == '?' or b == '?':
            q += 1
        else:
            if a > b:
                gt = True
            elif a < b:
                lt = True

    ans = pow(10, q, MOD)
    if lt and gt:
        print(ans)
        return
    
    le_cnt = ge_cnt = 1
    for a, b in zip(s, t):
        if a == '?' and b =='?':
            le_cnt = le_cnt * 55 % MOD
            ge_cnt = ge_cnt * 55 % MOD
        elif a == '?':
            x = int(b)
            le_cnt = le_cnt * (x + 1) % MOD
            ge_cnt = ge_cnt * (10 - x) % MOD
        elif b == '?':
            x = int(a)
            le_cnt = le_cnt * (10 - x) % MOD
            ge_cnt = ge_cnt * (x + 1) % MOD
    
    if not gt:
        ans -= le_cnt
    
    if not lt:
        ans -= ge_cnt
    
    if not lt and not gt:
        ans += pow(10, same, MOD)

    print(ans % MOD)


solve()
