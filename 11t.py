class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        t=0
        while i<j:
            t1=min(height[i],height[j])*(j-i)
            if t1>t:
                t=t1
            if height[i]>height[j]:
                j=j-1
            elif height[i]<height[j]:
                i=i+1
            else:
                i=i+1
                j=j-1
        return t
