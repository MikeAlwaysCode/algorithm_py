from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    w, h = map(int, input().split())

    if w == 1:
        print("bad")
    elif 2 <= w <= 3:
        if h >= 4:
            print("good")
        else:
            print("bad")
    elif 4 <= w <= 6:
        if h >= 2:
            print("good")
        else:
            print("bad")
    else:
        print("good")

    # if ( w > 1 and h >= 4 ) or ( w - 4 ) * h >= 3: 
    #     print("good")
    # else:
    #     print("bad")
    
    # if w == 1 or ( w < 4 and h < 4 ):
    #     print("bad")
    # else:
    #     print("good")

t = int(input())
for _ in range(t):
    solve()