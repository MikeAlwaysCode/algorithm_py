from collections import Counter

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        sc = 1
        for i in range(1, len(suits)):
            if suits[i] == suits[i-1]:
              sc += 1
        
        if sc == 5:
            return "Flush"
        
        c = Counter(ranks)
        print(c.most_common()[1])
        sc = c.most_common(1)[0][1] # max(c.values())
            
        if sc >= 3:
            return "Three of a Kind"
        elif sc >= 2:
            return "Pair"
        else:
            return "High Card"

class NumberContainers:

    def __init__(self):
        self.nums = defaultdict(list)
        self.id = dict()


    def change(self, index: int, number: int) -> None:
        if index in self.id:
            preNum = self.id[index]
            self.nums[preNum].remove(index)
        
        self.id[index] = number
                
        heapq.heappush(self.nums[number], index)
        # self.nums[number].sort()
            
        # print(self.nums)
                

    def find(self, number: int) -> int:
        if self.nums[number]:
            return heapq.nsmallest(1, self.nums[number])[0]
        else:
            return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    # lines = readlines()
    # while True:
    #     try:
    #         line = next(lines)
    #         # s = stringToString(line);
    #         s = line
            
    #         ret = Solution().bestHand(s)

    #         out = str(ret);
    #         print(out)
    #     except StopIteration:
    #         break
    r = [9,2,13,1,2]
    s = ["b","d","d","b","c"]
    print(Solution().bestHand(r, s))

if __name__ == '__main__':
    main()