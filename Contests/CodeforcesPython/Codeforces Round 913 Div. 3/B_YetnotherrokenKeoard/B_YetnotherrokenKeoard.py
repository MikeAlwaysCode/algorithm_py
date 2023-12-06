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
    s = input()
    u, l = [], []
    for i, c in enumerate(s):
        if c == 'b':
            if l:
                l.pop()
        elif c == 'B':
            if u:
                u.pop()
        elif c.islower():
            l.append((c, i))
        else:
            u.append((c, i))

    ans = []
    i = j = 0
    while i < len(u) and j < len(l):
        if u[i][1] < l[j][1]:
            ans.append(u[i][0])
            i += 1
        else:
            ans.append(l[j][0])
            j += 1
    while i < len(u):
        ans.append(u[i][0])
        i += 1
    while j < len(l):
        ans.append(l[j][0])
        j += 1
    print("".join(ans))


for _ in range(int(input())):
    solve()