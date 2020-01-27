class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def s(i,j):
            if j==0:
                b.append(a[:])
            if j>0 and i>0:
                a.append(')')
                s(i-1,j-1)
                del a[-1]
            if i<j:
                a.append('(')
                s(i+1,j)
                del a[-1]
        b=[]
        a=[]
        c=''
        d=[]
        s(0,n)
        for i in range(len(b)):
            c=''.join(b[i])
            d.append(c)
            c=''
        return d
