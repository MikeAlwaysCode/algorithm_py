import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# # region dfsconvert
# from types import GeneratorType
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc
# # endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    a, b, c, k = mint()
    if c < max(a, b) or c > max(a, b) + 1:
        print(-1)
        return
    
    for x in range(pow(10, a - 1), pow(10, a)):
        mny = max(pow(10, b - 1), pow(10, c - 1) - x)
        mxy = min(pow(10, b) - 1, pow(10, c) - 1 - x)
        if mxy < mny: continue
        if mxy - mny + 1 < k:
            k -= mxy - mny + 1
            continue
        print(x, "+", mny + k - 1, "=", x + mny + k - 1)
        return

    print(-1)

for _ in range(int(input())):
    solve()