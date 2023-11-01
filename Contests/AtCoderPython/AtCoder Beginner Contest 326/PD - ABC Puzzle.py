import sys
from itertools import combinations, permutations

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

t = "ABC"

def solve() -> None:
    n = sint()
    r = input()
    c = input()
    per = list(permutations(range(n), n))
    
    # A
    for p1 in per:
        cnt1 = [set() for _ in range(n)]
        for i, x in enumerate(p1):
            cnt1[i].add(x)
        for p2 in per:
            check = True
            for i, x in enumerate(p2):
                if x in cnt1[i]:
                    check = False
                    break
            if not check: continue
            cnt2 = [set() for _ in range(n)]
            for i, x in enumerate(p2):
                cnt2[i].add(x)
            for p3 in per:
                check = True
                for i, x in enumerate(p3):
                    if x in cnt1[i] or x in cnt2[i]:
                        check = False
                        break
                if not check: continue
                g = [['.'] * n for _ in range(n)]
                for i, x in enumerate(p1):
                    g[i][x] = 'A'
                for i, x in enumerate(p2):
                    g[i][x] = 'B'
                for i, x in enumerate(p3):
                    g[i][x] = 'C'
                cc = ['.'] * n
                for i in range(n):
                    rc = ''
                    for j in range(n):
                        if g[i][j] != '.':
                            if cc[j] == '.':
                                cc[j] = g[i][j]
                            if rc == '':
                                rc = g[i][j]
                    if rc != r[i]:
                        check = False
                        break
                    
                if not check:
                    continue
                
                if "".join(cc) != c:
                    check = False
                    
                if check:
                    print("Yes")
                    for row in g:
                        print("".join(row))
                    return

    print("No")

solve()