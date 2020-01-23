class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if ((target-nums[i]) in nums):
                for j in range(len(nums)):
                    if( nums[i]+nums[j]==target and i!=j):
                        return i,j
