class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def kk(i):
            t=1
            for j in range(1,i+1):
                t=t*j
            return t
        a=[]
        c=[]
        for i in range(1,n+1):
            a.append(i)
        def ss(k1,a1):
            if(len(a1)==1):
                c.append(a1[0])
            else:
                b=(k1-1)//kk(len(a1)-1)
                c.append(a1[b])
                if(k1%kk(len(a1)-1)==0):
                    k1=kk(len(a1)-1)
                else:
                    k1=k1%kk(len(a1)-1)
                del a1[b]
                ss(k1,a1)
        ss(k,a)
        c1=''
        for i in range(len(c)):
            c1=c1+str(c[i])
        return c1
