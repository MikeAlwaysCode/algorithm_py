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

p = []
for k in range(6):
    base = 10 ** k
    for x in p[:]:
        p.append(base + x)
    p.append(base)
p.sort()
s = {1}
for a in p[1:]:
    x = a
    while x <= 10 ** 5:
        for b in p:
            if x * b > 10 ** 5:
                break
            s.add(x * b)
        x *= a

def solve() -> None:
    n = sint()
    print("YES" if n in s else "NO")

for _ in range(int(input())):
    solve()
