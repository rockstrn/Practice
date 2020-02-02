class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        else:
            i=0
            j=len(nums)-1
            while i<=j :
                k=(i+j)//2
                if nums[k]==target:
                    break
                elif nums[k]<target:
                    i=k+1
                else:
                    j=k-1
            if(nums[k]<target):
                return k+1
            else:
                return k
