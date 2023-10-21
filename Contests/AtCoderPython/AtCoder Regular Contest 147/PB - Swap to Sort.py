from collections import Counter, defaultdict


def solve() -> None:
    n = int(input())

    arr = list(map(int, input().split()))

    ans = []

    def swap(c, p):
        ans.append((c, p + 1))
        q = p + 1 if c == 'A' else p + 2
        arr[p], arr[q] = arr[q], arr[p]

    for i in range(n):
        for j in range(n-2):
            if arr[j]%2 != arr[j+2]%2 and arr[j]%2 != (j+1)%2:
                swap('B', j)
    
    for i in range(n-1):
        if arr[i]%2 != arr[i+1]%2 and arr[i]%2 == i%2:
            swap('A', i)

    for i in range(n):
        for j in range(n-2):
            if arr[j] > arr[j+2]:
                swap('B', j)

    print(len(ans))
    for op in ans:
        print(op[0], op[1])

# t = int(input())
# for _ in range(t):
solve()