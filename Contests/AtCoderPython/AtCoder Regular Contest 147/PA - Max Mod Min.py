from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    
    while len(arr) != 1:
        arr.sort()
        m = arr[0]
        t = []
        ans += len(arr) - 1

        for i in range(len(arr)-1, 0, -1):
            k = arr[i] % m
            if k != 0:
                m = k
                t.append(k)
        t.append(arr[0])
        arr = t
                
    print(ans)

# t = int(input())
# for _ in range(t):
solve()