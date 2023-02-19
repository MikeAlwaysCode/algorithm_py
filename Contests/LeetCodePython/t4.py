class IntervalTree:
    def __init__(self, size):
        self.size = size
        self.interval_tree = [0 for _ in range(size*4)]
        self.lazys = [0 for _ in range(size*4)]

    def give_lay_to_son(self,p,l,r):
        interval_tree = self.interval_tree
        lazys = self.lazys
        if lazys[p] == 0:
            return
        mid = (l+r)//2
        interval_tree[p*2] = mid - l + 1 -  interval_tree[p*2]
        interval_tree[p*2+1] = r - mid - interval_tree[p*2+1]
        lazys[p*2] ^= 1
        lazys[p*2+1] ^=1
        lazys[p] = 0
        
    def update(self,p,l,r,x,y,val):
        """
        把[x,y]区域全变成val
        """
        if y < l or r < x:
            return 
        interval_tree = self.interval_tree    
        lazys = self.lazys        
        if x <= l and r<=y:
            interval_tree[p] = r-l+1-interval_tree[p]
            lazys[p] ^= 1
            return
        self.give_lay_to_son(p,l,r)
        mid = (l+r)//2
        if x <= mid:
            self.update(p*2,l,mid,x,y,val)
        if mid < y:
            self.update(p*2+1,mid+1,r,x,y,val)
        interval_tree[p] = interval_tree[p*2]+ interval_tree[p*2+1]    

    
    def query(self,p,l,r,x,y):
        """
        区间求和      """        
        
        if y < l or r < x:
            return 0
        if x<=l and r<=y:
            return self.interval_tree[p]
        self.give_lay_to_son(p,l,r)
        mid = (l+r)//2
        s = 0
        if x <= mid:
            s += self.query(p*2,l,mid,x,y)
        if mid < y:
            s += self.query(p*2+1,mid+1,r,x,y)
        return s
    
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        s = sum(nums2)
        tree = IntervalTree(n)
        for i,v in enumerate(nums1,start=1):
            if v:
                tree.update(1,1,n,i,i,1)
        ans = []
        for op,l,r in queries:
            if op == 1:
                tree.update(1,1,n,l+1,r+1,1)
            elif op == 2:
                s += l*tree.query(1,1,n,1,n)
            else:
                ans.append(s)
        return ans

