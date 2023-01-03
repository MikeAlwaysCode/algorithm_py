from typing import Counter

def solve() -> None:
    n = int(input())
    s = str(input())
    
    if Counter(s) != Counter("Timur"):
        print("No")
    else:
        print("Yes")

t = int(input())
for _ in range(t):
    solve()