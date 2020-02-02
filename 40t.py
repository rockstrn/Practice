class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def s(i,su,b):
            if(i<len(candidates)):
                if(su<target):
                    for j in range(i+1,len(candidates)):
                        b.append(candidates[j])
                        s(j,su+candidates[j],b[:])
                        del b[-1]
                if (su==target):
                    b.sort()
                    if(b not in a):
                        a.append(b[:])
        a=[]
        b=[]
        s(-1,0,b)
        return a
