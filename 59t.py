class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a=[]
        for i in range(n):
            a.append([1]*n)
        k=1
        for i in range((n+1)//2):
            for j in range(i,n-i):
                a[i][j]=k
                k=k+1
            for j in range(i+1,n-i-1):
                a[j][n-i-1]=k
                k=k+1
            if n!=2*i+1:
                for j in range(i,n-i):
                    a[n-1-i][n-j-1]=k
                    k=k+1
                for j in range(i+1,n-i-1):
                    a[n-1-j][i]=k
                    k=k+1
        return a
