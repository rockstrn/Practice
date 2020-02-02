class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c=[]
        for j in range(1,len(nums)):
            if nums[j] in nums[:j]:
                c.append(nums[j])
        def s(num):
            if(num==len(b)-1):
                a.append(b[:])
            i=num
            while i<len(nums):
                if b[i] in b[i+1:]:
                    i=i+1
                else:
                    b[num],b[i]=b[i],b[num]
                    s(num+1)
                    b[i],b[num]=b[num],b[i]
                    i=i+1
        a=[]
        b=nums
        s(0)
        return a
