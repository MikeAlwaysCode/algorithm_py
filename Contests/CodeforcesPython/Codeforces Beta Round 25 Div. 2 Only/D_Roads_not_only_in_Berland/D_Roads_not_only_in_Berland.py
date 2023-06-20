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
    n = sint()
    fa = list(range(n + 1))
    def find(x: int) -> int:
        cur = x
        while x != fa[x]:
            x = fa[x]
        while cur != x:
            fa[cur], cur = x, fa[cur]
        return x
    
    def union(x: int, y: int):
        x, y = find(x), find(y)
        if x == y: return
        if x > y: x, y = y, x
        fa[y] = x
    
    d, a = [], []
    for _ in range(n - 1):
        u, v = mint()
        fu, fv = find(u), find(v)
        if fu == fv:
            d.append((u, v))
        else:
            union(fu, fv)
    f1 = find(1)
    for i in range(2, n + 1):
        fi = find(i)
        if fi != f1:
            a.append((1, i))
            union(f1, fi)
    
    print(len(d))
    for (u1, v1), (u2, v2) in zip(d, a):
        print(u1, v1, u2, v2)

solve()