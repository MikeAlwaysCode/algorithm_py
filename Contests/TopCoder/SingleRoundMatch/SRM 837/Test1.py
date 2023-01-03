class StairsFromBlocks:
    def build(self, W, H):
        n = len(W)
        block = sorted(zip(H, W), reverse=True)

        wx = 0
        area = 0
        prew = 0
        for i in range(n):
            area += block[i][0] * block[i][1]
            cur = prew + block[i][0] + block[i][1] - 1
            # print(i, block[i][0], block[i][1], cur)
            wx = max(wx, prew + block[i][0] + block[i][1] - 1)
            prew += block[i][1]

        print(wx, area)
        return (wx + 1) * wx // 2 - area
        
def main():
    W = (2, 2, 2)
    H = (1, 1, 1)
    sol = StairsFromBlocks()

    print(sol.build(W, H))

if __name__ == '__main__':
    main()