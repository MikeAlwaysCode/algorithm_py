import sys
# from collections import deque

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
    n, q = mint()
    dragon = list((x, 0) for x in range(n, 0, -1))
    for _ in range(q):
        qry = input().split()
        if qry[0] == '1':
            x, y = dragon[-1]
            if qry[1] == 'U':
                y += 1
            elif qry[1] == 'D':
                y -= 1
            elif qry[1] == 'R':
                x += 1
            else:
                x -= 1
            dragon.append((x, y))
        else:
            p = len(dragon) - int(qry[1])
            print(*dragon[p])


solve()
