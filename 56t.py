class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a=[]
        j=len(intervals)-1
        while j>0:
            for i in range(j):
                if (intervals[j][1]<intervals[i][0] or intervals[j][0]>intervals[i][1]):
                    continue
                else:
                    intervals[i][0]=min(intervals[i][0],intervals[j][0])
                    intervals[i][1]=max(intervals[i][1],intervals[j][1])
                    intervals[j][0]='c'
                    intervals[j][1]='c'
                    break
            j=j-1
        for i in range(len(intervals)):
            if intervals[i][1]!='c':
                a.append(intervals[i])
        return a
