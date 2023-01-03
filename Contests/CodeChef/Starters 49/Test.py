from collections import Counter

def main():
    n, k = 1, 1
    s = "1"

    a, b = 0, 0
    for x in s:
        if x == '0':
            a += 1
        else:
            b += 1

    ans = abs(( a + k - 1 ) // k - ( b + k - 1 ) // k)
    if ans == 0 and a != b: ans = 1
    
    print(ans)

if __name__ == '__main__':
    main()