
def solve() -> None:
    # MX = 10 ** 9

    n, k = map(int, input().split())
    
    m = n * (n + 1) // 2
    
    # if n == MX and m % k != 0:
    #     print(-1)
    #     return
    
    ans = [i for i in range(1, n+1)]

    if m % k != 0:
        # ans[-1] += k - (m % k)
        d = k - (m % k)
        p = d // n
        q = d % n
        for i in range(n - 1, -1, -1):
            ans[i] += p
            if n - i <= q:
                ans[i] += 1
        
    print(*ans)
    
solve()