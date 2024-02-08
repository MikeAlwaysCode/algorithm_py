import sys
# from random import randint

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
    n, m, k = mint()
    A = ints()
    B = ints()
    sa = set([x for x in A if x <= k])
    sb = set([x for x in B if x <= k])
    cnta = cntb = both = 0
    for i in range(1, k + 1):
        if i in sa and i in sb:
            both += 1
        elif i in sa:
            cnta += 1
        elif i in sb:
            cntb += 1
        else:
            print("NO")
            return
    '''
    h = randint(1, 1 << 30)
    sa = set([x ^ h for x in A if x <= k])
    sb = set([x ^ h for x in B if x <= k])
    cnta = cntb = both = 0
    for i in range(1, k + 1):
        if i ^ h in sa and i ^ h in sb:
            both += 1
        elif i ^ h in sa:
            cnta += 1
        elif i ^ h in sb:
            cntb += 1
        else:
            print("NO")
            return
    '''
    # print(cnta, cntb, both)
    print("YES" if cnta + both >= k // 2 and cntb + both >= k // 2 else "NO")


for _ in range(int(input())):
    solve()
