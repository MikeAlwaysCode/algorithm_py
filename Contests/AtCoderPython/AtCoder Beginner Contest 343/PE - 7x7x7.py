import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    v1, v2, v3 = mint()
    
    if v1 + v2 * 2 + v3 * 3 != 1029:
        print("No")
        return
    
    if v2 == v3 == 0:
        print("Yes")
        print(0, 0, 0, 7, 0, 0, 0, 7, 0)
        return
    
    a1 = b1 = c1 = 0
    
    for a2 in range(8):
        for b2 in range(8):
            for c2 in range(8):
                v12 = (7 - a2) * (7 - b2) * (7 - c2)
                if v12 < v3:
                    continue
                for a3 in range(-7, 8):
                    for b3 in range(-7, 8):
                        for c3 in range(-7, 8):
                            v13 = (7 - abs(a3)) * (7 - abs(b3)) * (7 - abs(c3))
                            v23 = max(7-abs(a3-a2),0)*max(7-abs(b3-b2),0)*max(7-abs(c3-c2),0)
                            v33 = max(0, min(a1, a2, a3) + 7 - max(a1, a2, a3)) * max(0, min(b1, b2, b3) + 7 - max(b1, b2, b3)) * max(0, min(c1, c2, c3) + 7 - max(c1, c2, c3))
                            if v33 == v3 and v12 + v13 + v23 - v3 * 3 == v2:
                                print("Yes")
                                print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
                                return
    print("No")

solve()
