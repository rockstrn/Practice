class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0 for _ in range(len(nums)+1)]
        for i in range(1,len(nums)+1):
            dp[i]=max(dp[i-1]+nums[i-1],nums[i-1])
        return max(dp[1:])
