def solve() -> None:
    n = int(input())
    s1 = str(input())
    s2 = str(input())

    s1 = s1.replace("G", "B")
    s2 = s2.replace("G", "B")

    if s1 == s2:
        print("Yes")
    else:
        print("No")

t = int(input())
for _ in range(t):
    solve()