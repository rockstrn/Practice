class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a=[]
        def s(num,b):
            if num==target:
                b.sort()
                if(b not in a):
                    a.append(b)
            elif num<target:
                for i in  candidates:
                    b.append(i)
                    s(num+i,b[:])
                    del b[-1]
        h=[]
        s(0,h)
        return a
