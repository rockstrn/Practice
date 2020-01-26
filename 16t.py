class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        u=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if nums[i]>target//3:
                break
            j=i+1
            k=len(nums)-1
            while j<k:
                if target-nums[i]-nums[j]-nums[k]==0:
                    return target
                elif target-nums[i]-nums[j]-nums[k]>0:
                    if abs(u-target)>abs(target-nums[i]-nums[j]-nums[k]):
                        u=nums[i]+nums[j]+nums[k]
                    j=j+1
                else:
                    if abs(u-target)>abs(target-nums[i]-nums[j]-nums[k]):
                        u=nums[i]+nums[j]+nums[k]
                    k=k-1
        return u
