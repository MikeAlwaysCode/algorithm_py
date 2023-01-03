N, A, B = map(int, input().split())
if N < A:
    print(0)
elif A <= B:
    print(N - A + 1)
else:
    ans = (N//A - 1) * B
    ans += min(B, N % A + 1)
    print(ans)