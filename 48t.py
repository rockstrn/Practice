class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i=0
        q=len(matrix)
        while i < q//2:
            for j in range(i,q-i-1):
                a=matrix[j][q-i-1]   
                matrix[j][q-i-1]=matrix[i][j] 
                b=matrix[q-i-1][q-1-j]  
                matrix[q-i-1][q-1-j]=a  
                c=matrix[q-1-j][i]   
                matrix[q-1-j][i]=b  
                matrix[i][j]=c
            i=i+1
