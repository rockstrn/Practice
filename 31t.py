class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ma=nums[len(nums)-1]
        k=len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<ma:
                k=i
                break
            else:
                ma=nums[i]
        if k==len(nums):
            nums.sort()
        else:
            k1=nums.index(ma,k)
            for i in range(k+1,len(nums)):
                if nums[i]>nums[k] and nums[i]<ma:
                    ma=nums[i]
                    k1=i
            nums[k],nums[k1]=nums[k1],nums[k]
            for i in range(k+1,len(nums)):
                for j in range(k+1,len(nums)+k-i):
                    if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
