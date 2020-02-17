class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a=[]
        if len(matrix)==0:
            return a
        i=min(len(matrix),len(matrix[0]))
        i=(i+1)//2
        for j in range (i) :
            for k in range (j,len(matrix[0])-j):
                a.append(matrix[j][k])
            for k in range (j+1,len(matrix)-1-j):
                a.append(matrix[k][len(matrix[0])-j-1])
            if (j+1<=len(matrix)-1-j):
                for k in range (j,len(matrix[0])-j):
                    a.append(matrix[len(matrix)-1-j][len(matrix[0])-k-1])
            if (j+1<len(matrix[0])-j):
                for k in range (j+1,len(matrix)-1-j):
                    a.append(matrix[len(matrix)-1-k][j])
        return a
