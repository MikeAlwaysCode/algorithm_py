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
    m = sint()
    st = list(input())
    n = e = w = s = 0
    for c in st:
        if c == 'N':
            n += 1
        elif c == 'E':
            e += 1
        elif c == 'S':
            s += 1
        else:
            w += 1
    if (n + s) & 1 or (e + w) & 1:
        print("NO")
        return
    ans = ['H'] * m
    final_n = (n - s) // 2
    final_e = (e - w) // 2
    cn = ce = 0
    force = (n - s) == 0 and (e - w) == 0
    for i, c in enumerate(st):
        if c == 'N':
            if cn < final_n or force:
                ans[i] = 'R'
                cn += 1
        elif c == 'E':
            if ce < final_e or force:
                ans[i] = 'R'
                ce += 1
        elif c == 'S':
            if cn > final_n or force:
                ans[i] = 'R'
                cn -= 1
        else:
            if ce > final_e or force:
                ans[i] = 'R'
                ce -= 1
        force = False
    if ans.count('H') == 0 or ans.count('R') == 0:
        print("NO")
        return
    print("".join(ans))


for _ in range(int(input())):
    solve()
