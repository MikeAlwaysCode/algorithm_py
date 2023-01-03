from collections import Counter, defaultdict

def solve() -> None:
    n, k = map(int, input().split())
    s = str(input())
    ans = ["0"] * n
    op = [0] * n

    if k == 1:
        print("".join(ans))
        return

    f = idx = 0
    for i in range(n-k+1):
        if i >= k:
            if op[i-k]:
                f ^= op[i-k]
        if int(s[i]) ^ f:
            f ^= 1
            op[i] = 1
    # print(op)
    # print(f)
    for i in range(n-k+1, n):
        if op[i-k]:
            f ^= op[i-k]
        ans[i] = str(int(s[i]) ^ f)

    print("".join(ans))

t = int(input())
for _ in range(t):
    solve()