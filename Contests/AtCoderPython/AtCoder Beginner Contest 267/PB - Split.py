from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    S = str(input())

    cols = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]

    if S[0] == '1':
        print("No")
        return

    pins = [0] * 7
    for i, x in enumerate(S):
        pins[cols[i]] += x == '1'
    
    chk = [1, 0, 1]
    j = 0
    for i in range(7):
        if (pins[i] == 0) == (chk[j] == 0):
            j += 1
        if j > 2:
            print("Yes")
            return

    print("No")
    
        
solve()