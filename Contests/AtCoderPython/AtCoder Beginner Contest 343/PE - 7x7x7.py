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
    s = 1029
    if v1 + v2 * 2 + v3 * 3 != s:
        print("No")
        return
    if v2 == v3 == 0:
        print("Yes")
        print(0, 0, 0, 7, 0, 0, 0, 7, 0)
        return
    a1 = b1 = c1 = 0
    '''
    for a2 in range(15):
        for b2 in range(15):
            for c2 in range(15):
                v12 = max(0, 7 - a2) * max(0, 7 - b2) * max(0, 7 - c2)
                if v12 > v2:
                    continue
                for a3 in range(15):
                    for b3 in range(15):
                        for c3 in range(15):
                            v13 = max(0, 7 - a3) * max(0, 7 - b3) * max(0, 7 - c3)
                            v23 = max(0, min(a2 + 7 - a3, a3 + 7 - a2)) * max(0, min(b2 + 7 - b3, b3 + 7 - b2)) * max(0, min(c2 + 7 - c3, c3 + 7 - c2))
                            v33 = max(0, min(a1, a2, a3) + 7 - max(a1, a2, a3)) * max(0, min(b1, b2, b3) + 7 - max(b1, b2, b3)) * max(0, min(c1, c2, c3) + 7 - max(c1, c2, c3))
                            if v33 == v3 and v12 + v13 + v23 - v3 * 3 == v2:
                                print("Yes")
                                print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
                                return
    '''
    
    if v3 == 0:
        for a2 in range(7):
            for b2 in range(7):
                for c2 in range(7):
                    v21 = (7 - a2) * (7 - b2) * (7 - c2)
                    if v21 > v2:
                        continue
                    v22 = v2 - v21
                    for a3 in range(a2, a2 + 8):
                        for b3 in range(b2, b2 + 8):
                            for c3 in range(c2, c2 + 8):
                                if a3 < 7 and b3 < 7 and c3 < 7:
                                    continue
                                if (a2 + 7 - a3) * (b2 + 7 - b3) * (c2 + 7 - c3) == v22:
                                    print("Yes")
                                    print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
                                    return
    else:
        for x in range(8):
            for y in range(x, 8):
                for z in range(y, 8):
                    if x * y * z < v3:
                        continue
                    a2, b2, c2 = 7 - x, 7 - y, 7 - z
                    v12 = x * y * z
                    for a3 in range(a2 + 8):
                        for b3 in range(b2 + 8):
                            for c3 in range(c2 + 8):
                                # v12 = max(0, 7 - a2) * max(0, 7 - b2) * max(0, 7 - c2)
                                v13 = max(0, 7 - a3) * max(0, 7 - b3) * max(0, 7 - c3)
                                v23 = max(0, min(a2 + 7 - a3, a3 + 7 - a2)) * max(0, min(b2 + 7 - b3, b3 + 7 - b2)) * max(0, min(c2 + 7 - c3, c3 + 7 - c2))
                                v33 = max(0, min(a1, a2, a3) + 7 - max(a1, a2, a3)) * max(0, min(b1, b2, b3) + 7 - max(b1, b2, b3)) * max(0, min(c1, c2, c3) + 7 - max(c1, c2, c3))
                                if v33 == v3 and v12 + v13 + v23 - v3 * 3 == v2:
                                    print("Yes")
                                    print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
                                    return
                                
    print("No")

solve()
