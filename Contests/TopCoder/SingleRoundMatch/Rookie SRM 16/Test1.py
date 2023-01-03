class Sum21:
    def countWays(self, x):
        arr = list(x)
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == 21:
                    ans += 1
                elif arr[i] + arr[j] > 21:
                    break
        return ans
        
def main():
    r1, c1, r2, c2, s = 4, 7, 4, 7, 12
    # sol = WordleColors()

    # print(sol.color(r1, c1, r2, c2, s))

if __name__ == '__main__':
    main()