from math import lcm


def solve() -> None:
    a, b, c, d = map(int, input().split())

    k = lcm(b, d)

    a *= k // b
    c *= k // d
    
    a, c = max(a, c), min(a, c)
    if a == c:
        print(0)
    elif c == 0 or a%c == 0:
        print(1)
    else:
        print(2)

t = int(input())
for _ in range(t):
    solve()