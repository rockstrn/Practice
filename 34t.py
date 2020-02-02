class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        k=(len(nums)-1)//2
        k1=k
        k2=k
        if(len(nums)==0):
            return[-1,-1]
        while i<j:
            if(nums[k]>target):
                j=k-1
                k=(i+j)//2
            elif nums[k]<target:
                i=k+1
                k=(i+j)//2
            else:
                break
        if(nums[k]!=target):
            return [-1,-1]
        else:
            k1=k
            k2=k
            while k1!=0:
                if(nums[k1-1]==target):
                    k1=k1-1
                else:
                    break
            while k2+1<len(nums):
                if(nums[k2+1]==target):
                    k2=k2+1
                else:
                    break
            return[k1,k2]
