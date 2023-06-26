import itertools
import math
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
    n, m = mint()
    seg = []
    for _ in range(m):
        seg.append(tuple(mint()))

    q = sint()
    change = []
    for _ in range(q):
        change.append(sint())
    
    def check(x: int) -> bool:
        nums = [0] * n
        for i in change[:x]:
            nums[i - 1] = 1
        pres = list(itertools.accumulate(nums, initial = 0))
        for l, r in seg:
            k = (r - l + 3) // 2
            if pres[r] - pres[l - 1] >= k: return True
        return False

    l, r = 0, q
    while l <= r:
        mid = l + r >> 1
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
            
    print(-1 if l > q else l)

for _ in range(int(input())):
    solve()