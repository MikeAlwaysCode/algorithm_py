n = int(input())
arr = list(map(int, input().split()))
ans = sum(arr[i] == arr[i+n] for i in range(n))
print(ans)