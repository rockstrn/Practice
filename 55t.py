class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[0 for _ in range(len(nums))]
        dp[-1]=1
        for i in range(len(dp)-2,-1,-1):
            for j in range(nums[i]):
                if dp[i+j+1]==1:
                    dp[i]=1
                    break
        return bool(dp[0])
