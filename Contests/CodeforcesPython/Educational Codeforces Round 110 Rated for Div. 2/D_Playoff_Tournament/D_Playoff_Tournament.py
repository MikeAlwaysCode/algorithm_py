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
    k = sint()
    s = list(reversed(input()))

    n = 1 << k
    cnt = [1] * (n * 2)

    def update(i: int):
        if s[i] == '0':
            cnt[i] = cnt[i * 2 + 2]
        elif s[i] == '1':
            cnt[i] = cnt[i * 2 + 1]
        else:
            cnt[i] = cnt[i * 2 + 1] + cnt[i * 2 + 2]
    
    for i in range(n - 2, -1, -1):
        update(i)

    for _ in range(sint()):
        qry = input().split()
        p = n - int(qry[0]) - 1
        s[p] = qry[1]
        while p >= 0:
            update(p)
            p = (p - 1) // 2
        print(cnt[0])

solve()