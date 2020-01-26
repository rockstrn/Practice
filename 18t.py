class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)-3):
            if nums[i]>target//4:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        a.append([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                        while k<len(nums) and nums[k]==nums[k-1]:
                            k=k+1
                        l=l-1
                        while l>j and nums[l]==nums[l+1]:
                            l=l-1
                    elif nums[i]+nums[j]+nums[k]+nums[l]<target:
                        k=k+1
                        while k<len(nums) and nums[k]==nums[k-1]:
                            k=k+1
                    else:
                        l=l-1
                        while l>j and nums[l]==nums[l+1]:
                            l=l-1
        return a
