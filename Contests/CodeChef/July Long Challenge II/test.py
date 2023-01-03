
def solve(n: int, m: int):
    c = m // n
    a = m // c
    b = a * c
    
    return (a, b)

M = 10 ** 9
N = 10 ** 5
for n in range(1, N+1):
    for m in range(1, M+1):
        print(n, m, solve(n, m), file = open("log.txt", mode = "a", encoding = "utf-8"))

print("Finished")